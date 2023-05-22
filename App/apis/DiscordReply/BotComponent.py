from interactions import Extension, listen, Client,\
                        Modal, ShortText, ParagraphText, ModalContext
from interactions.api.events import Component

from . import BotSettings, PostAgent, SystemQueue, DQueueID, DQueueFQID

from .exts.CPMethod import ButtonClick
from .exts.CLMethod import ChannelSwitch

'''
Component Item Class
'''
class BotComponentCls(Extension):
    def __init__(self, client: Client) -> None:
        self.KeyMap = {        
            'U1': 0,
            'U2': 1,
            'U3': 2,
            'U4': 3,
            'V1': 4,
            'V2': 5,
            'V3': 6,
            'V4': 7,
            "Refresh": 8,
            "VariationU": 9,
            "Remaster": 10,
            "LightU": 11,
            "DetailU": 12,
            "RealityU": 13,
        }

    @listen()
    async def on_component(self, event: Component, **kwargs):
        ctx = event.ctx

        # Fast / Relax 模式
        if "Fast" in ctx.custom_id or "Relax" in ctx.custom_id:
            response = PostAgent.Fast() if ctx.custom_id == "Fast" else PostAgent.Relax()

            if response[0]:
                await ctx.edit_origin(components = ButtonClick(ctx, Switch=["BotInit", "Speed"]))
                BotSettings["BotInit"]["Speed"] = ctx.custom_id
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('模式切换至:{}'.format(ctx.custom_id))

            else:
                await ctx.send(response[1])

        # U / V 模式
        elif len(ctx.custom_id) == 2 and ("U" in ctx.custom_id or "V" in ctx.custom_id):
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})
            
            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            if "U" in ctx.custom_id:
                response = PostAgent.Upscale(str(ctx.custom_id)[1], targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
                QID = DQueueFQID
            else:
                response = PostAgent.Variation(str(ctx.custom_id)[1], targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
                QID = DQueueID

            if response[0]:
                _insert = SystemQueue.insert_queue(QID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('正在进行操作：{}细分'.format(ctx.custom_id), ephemeral=True)
            else:
                await ctx.send(response[1])

        # Refresh 模式
        elif ctx.custom_id == "Refresh":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.Refresh(0, targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney重新生成照片中...', ephemeral=True)

            else:
                await ctx.send(response[1])

        # BlendG 模式 待评估  需求量感觉没多少


        # DescribeU 模式 现在获得不了embed的image信息 等后面更新
        elif ctx.custom_id == "DescribeU":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            image = ctx.message.embeds[0].image
            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            
            response = PostAgent.Describe(image, "", channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueFQID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"DC", "Image": image.__getattribute__("url")})
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney描述生成照片中...', ephemeral=True)

        # VariationU 模式
        elif ctx.custom_id == "VariationU":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.Variation(1, targetDict["TargetID"], targetDict["TargetHash"], solo=True, channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney细分发散模式生成照片中...', ephemeral=True)

            else:
                await ctx.send(response[1])

        # Remaster 模式
        elif ctx.custom_id == "Remaster":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.Remaster(1, targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney重复发散模式生成照片中...', ephemeral=True)

            else:
                if "Invalid Form Body" in response[1]:
                    await ctx.send("该按钮在此消息上不可用，敬请期待后续开发")
                else:
                    await ctx.send(response[1])

        # LightU 模式
        elif ctx.custom_id == "LightU":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.LUpscale(1, targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney光影重复发散模式生成照片中...', ephemeral=True)

            else:
                if "Invalid Form Body" in response[1]:
                    await ctx.edit_origin(components = ButtonClick(ctx))
                    signalChannel = self.client.get_channel(int(ctx.channel_id))
                    await signalChannel.send('该按钮在此消息上不可用，敬请期待后续开发')
                else:
                    await ctx.send(response[1])
        
        # DetailU 模式
        elif ctx.custom_id == "DetailU":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.DUpscale(1, targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney细节重复发散模式生成照片中...', ephemeral=True)

            else:
                if "Invalid Form Body" in response[1]:
                    await ctx.edit_origin(components = ButtonClick(ctx))
                    signalChannel = self.client.get_channel(int(ctx.channel_id))
                    await signalChannel.send('该按钮在此消息上不可用，敬请期待后续开发')
                else:
                    await ctx.send(response[1])
            
        # RealityU 模式
        elif ctx.custom_id == "RealityU":
            ChannelSwitch(ctx)
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.BUpscale(1, targetDict["TargetID"], targetDict["TargetHash"], channel=_channel)
            if response[0]:
                _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"BT{}".format(self.KeyMap[ctx.custom_id])}, UpJob=targetDict["JobID"], otherKey="#{}".format(self.KeyMap[ctx.custom_id]))
                await ctx.edit_origin(components = ButtonClick(ctx, disable = False))
                signalChannel = self.client.get_channel(int(ctx.channel_id))
                await signalChannel.send('DandJourney真实重复发散模式生成照片中...', ephemeral=True)

            else:
                if "Invalid Form Body" in response[1]:
                    await ctx.edit_origin(components = ButtonClick(ctx))
                    signalChannel = self.client.get_channel(int(ctx.channel_id))
                    await signalChannel.send('该按钮在此消息上不可用，敬请期待后续开发')
                else:
                    await ctx.send(response[1])

        # Remaster With Prompt
        elif ctx.custom_id == "RePrompt":
            targetDict = {}
            for _emb in ctx.message.embeds[0].fields: targetDict.update({_emb.name: _emb.value})

            my_modal = Modal(
                ParagraphText(label="添加辅助描述词", custom_id="Prompt"),
                ShortText(label="描述词权重", custom_id="Weight", placeholder="0-15之间的整数,数字越大占比越高"),
                title="描述词添加",
            )

            await ctx.send_modal(modal=my_modal)
            modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
            await modal_ctx.send(modal_ctx.responses["Prompt"])


def setup(bot):
    print("Init BotComponent.py")
    BotComponentCls(bot)