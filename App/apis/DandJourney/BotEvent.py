from . import bot, interactions, agentBot
from . import UVComponent, MakeVComponent

from .utils.utils import CreateMsg, CreateAgency


def initCommand():
    print("Init BotEvent.py")


@bot.event
async def on_ready():
    print("程序初始化完毕，当前频道：{}".format(agentBot["BotCode"]["SERVER_ID"]))


@bot.event
async def on_message_reaction_add(message):
    """
    反应监听
    方法已弃用
    有需要自己添加
    """
    if message.member.user.bot : return    
    return


@bot.event
async def on_message_create(message):
    """
    消息监听
    """
    if message.content == "": return

    if message.author.bot:
        try:
        # 减少判断条件数量，其他归并做忽略处理 
        # 经测试无法删除MidJourney的原始消息，否则会404_No_Message，如果觉得重复生成比较烦，可以专门开一个区用来存放生成的内容

        # 条件1：当消息为Midjourney发送，且内容包含所需组件，则自动回复这条消息获得targetID 与 targetHash
            if message.author.username == "Midjourney Bot" and "U" in message.components[0].components[0].label:
                agency = CreateAgency(message, "UV")
                await message.reply(content = agency)

            if message.author.username == "Midjourney Bot" and "Make Variations" in message.components[0].components[0].label:
                agency = CreateAgency(message, "MV")
                await message.reply(content = agency)

        # 条件2：当消息为Bot发送，且内容为GET UV，则获得targetID 与 targetHash
            if message.author.username == agentBot["BotInfo"]["Name"] and "Get Bot Message for UV" in message.content:
                ReplyMsg = CreateMsg(message)
                await message.edit(content = ReplyMsg, components = UVComponent)

        # 条件3：当消息为Midjourney发送，且内容包含Make组件，则回复这条消息并标识为细化终图
            if message.author.username == agentBot["BotInfo"]["Name"] and "Get Bot Message for MV" in message.content: 
                ReplyMsg = CreateMsg(message)
                await message.edit(content = ReplyMsg, components = MakeVComponent)

        except IndexError:
            pass

    return



# ------------------------------------------------- #
initCommand()
# ------------------------------------------------- #