from interactions import Extension, listen, Client

from interactions.api.events import MessageCreate, MessageUpdate

from . import BotSettings, PostAgent, SystemQueue, DQueueFQID

from .exts.CPMethod import CreateMultipleButtons

from .utils.MsgGene import CreateAgency, CreateMsg, QueueParse
from .utils.EmbGene import ImageEmb, DescribeEmb

'''
Event Listen Class
'''
class BotEventCls(Extension):
    def __init__(self, client: Client) -> None:
        self.client = client

        UVComponent = CreateMultipleButtons(ButtonName = ["U1", "U2", "U3", "U4", "V1", "V2", "V3", "V4", "🔁 Refresh", "🈴 Mix Them"], 
                                            custom_idDic = {"🔁 Refresh":"Refresh", "🈴 Mix Them":"BlendG"}, padding = [4,4,2], disableDic = {"🈴 Mix Them": True}, instantiation=True)
        # 注意,新增的三个U按钮有执行顺序(),且发送的是消息更新on_MessageUpdate,用on_MessageCreate接不到
        # 鉴于目前确实按钮时多时少,等稳定了会把UV并入一条队列中,减少空间占用
        # 所以发现有些按钮点不了了就先不用提Issus
        MakeVComponent = CreateMultipleButtons(ButtonName = ["🔉 Describe", "🎁 Make Variations", "🔄 Remaster", "💡 Add Prompt", "🌈 Light Refinement", "🌈 Detail Refinement", "🌈 Reality Refinement"], 
                                            custom_idDic = {"🔉 Describe": "DescribeU", "🎁 Make Variations": "VariationU", "🔄 Remaster": "Remaster", "💡 Add Prompt": "RePrompt", 
                                                            "🌈 Light Refinement": "LightU", "🌈 Detail Refinement": "DetailU", "🌈 Reality Refinement": "RealityU"}, 
                                            disableDic={"🔉 Describe": True, "💡 Add Prompt": True}, padding = [2,2,3], instantiation = True)
        
        self.UVComponent = UVComponent[1] if UVComponent[0] else None
        self.MakeVComponent = MakeVComponent[1] if MakeVComponent[0] else None
        self.describeBox = []
        print("按钮实例化完毕")
        

    @listen()
    async def on_ready(self):
        print("Bot Ready!")
        print(SystemQueue.queueAllItem(length=True))

    @listen()
    async def on_MessageUpdate(self, event: MessageUpdate, **kwargs):

        message = event.after
        if message.author.bot:
            try:
                if message.author.username == "Midjourney Bot" and message.interaction.name == "describe":
                    if message.id not in self.describeBox:

                        self.describeBox.append(message.id)
                        # 临时写法,只能用在Discord上面
                        # Describe的问题很大,传递的照片一旦出问题很容易堵塞队列,在按时间清除队列元素写法出来前不建议使用
                        # API用法不要用这种写法,会堵塞队列影响User绑定
                        # 不建议加组件按钮去实现功能,有时候它自己会生成一些黑名单的词,导致阻塞进程
                        _DiscordQueue = SystemQueue.find_queue(DQueueFQID)[1].find("Mode", "DC")[0]
                        _emb = DescribeEmb(message.embeds[0].description, _DiscordQueue["Image"])

                        signalChannel = self.client.get_channel(int(_DiscordQueue["Channel"] if BotSettings["BotOpt"]["AGENT_SIGN"] else message.channel.id))
                        await signalChannel.send(content = "<@{}>".format(_DiscordQueue["User"]), embeds = _emb, attachments=[])
                        SystemQueue.delete_queue_value(DQueueFQID, _DiscordQueue["JobID"])
                        print(SystemQueue.queueAllItem(length=True))
                    else:
                        self.describeBox.remove(message.id)
            except AttributeError as e:
                pass




    @listen()
    async def on_MessageCreate(self, event: MessageCreate, **kwargs):
        message = event.message
        if message.content == "": return
        if message.author.bot:
            try:
            # 减少判断条件数量，其他归并做忽略处理 
            # 经测试无法删除MidJourney的原始消息，否则会404_No_Message，如果觉得重复生成比较烦，可以专门开一个区用来存放生成的内容
            
            # 前置条件 取出队列的数据
                Queue_msg = QueueParse(message.content, SystemQueue)
            
            # 条件1：当消息为Midjourney发送，且能够获取相关的信息，则自动回复这条消息获得targetID 与 targetHash

            # update 1:这里有bug,暂时没办法通过消息去获得队列中按钮触发的队列信息(JobID不能通过按钮传递)
            #          现在采用时间差的方式实现该功能,若Midjourney的回复不按照时间顺序触发,则会引发消息转发对象异常的bug
            #          update 1 for Discord: 目前采用两个队列,分别记录需要时间生成(如Imagine/Blend等指令)的任务与不需要时间的任务(U细分/Describe)
            #          update 1 for Api:在获取到下一次消息后将上一次的迭代消息删除,或在发送请求后暂停user的消息接收

                if message.attachments and Queue_msg[0] and message.author.username == "Midjourney Bot":

                    msgID = Queue_msg[1][1].queue_name
                    Qmsg = Queue_msg[1][1].find("JobID",Queue_msg[1][0])
                    if not Qmsg:
                        Qmsg = Queue_msg[1][1].find("JobID",Queue_msg[1][0], dim = -2)
                    agency = CreateAgency(message, Qmsg[0], msgID)
                    await message.reply(content = agency)

            # 条件2：当消息为Bot发送，且内容关于图像操作，则获得对象,此时指向图片的UV细分
                if message.author.username == BotSettings["BotInfo"]["Name"] and "Get Bot Message for" in message.content:
                    _mode, _user, _embed, _channel, _JobID, _msgJobID = ImageEmb(message)
                    signalChannel = self.client.get_channel(int(_channel if BotSettings["BotOpt"]["AGENT_SIGN"] else message.channel.id))
                    if _mode == "UV" or ("BT" in _mode and 4 <= int(_mode[2:]) < 14):
                        await signalChannel.send(content = _user, components = self.UVComponent, embeds = _embed, attachments=[])
                    elif _mode == "MV" or ("BT" in _mode and int(_mode[2:]) < 4):
                        await signalChannel.send(content = _user, components = self.MakeVComponent, embeds = _embed, attachments=[])
                    else:
                        pass
                    SystemQueue.delete_queue_value(_msgJobID, _JobID)
                    await message.delete(delay=5)
                    print(SystemQueue.queueAllItem(length=True))
            
                
            except IndexError as e:
                pass

        return


def setup(bot):
    print("Init BotEvent.py")
    BotEventCls(bot)