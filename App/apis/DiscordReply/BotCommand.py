from interactions import slash_command, SlashContext, Extension, Client
import interactions

from App.apis import DQueueFQID

from . import BotSettings, PostAgent, SystemQueue, DQueueID

from .exts.PPMethod import PromptMix
from .exts.CLMethod import ChannelSwitch
from .exts.CPMethod import CreateMultipleButtons

from .utils.EmbGene import HelpEmb, AboutEmb
from .utils import PromptCls


'''
Slash Command Class
'''
class BotCommandCls(Extension):
    def __init__(self, client: Client) -> None:
        self.client = client

    @slash_command(name="dtest", description="DandJourney调试模式")
    async def dtest(self, ctx: SlashContext, **kwargs):
        await ctx.send("Hello World 1")



    @slash_command(name="dsettings", description="DandJourney设置")
    async def dsettings(self, ctx: SlashContext, **kwargs):
        VersionComponent = CreateMultipleButtons(ButtonName = ["Fast", "Relax"], 
                                                styleDic={BotSettings["BotInit"]["Speed"]: 1}, 
                                                disableDic={BotSettings["BotInit"]["Speed"]: True}, 
                                                padding = [2], instantiation = True)
        VersionComponent = VersionComponent[1] if VersionComponent[0] else None
        await ctx.send(content = "机器人设置", components = VersionComponent)

    @slash_command(name="dabout", description="关于DandJourney")
    async def dabout(self, ctx: SlashContext, **kwargs):
        await ctx.send(embeds = AboutEmb())

    @slash_command(name="dhelp", description="DandJourney帮助手册")
    async def dhelp(self, ctx: SlashContext, **kwargs):
        await ctx.send(embeds = HelpEmb())

    @slash_command(name="dj", description="DandJourney图像生成")
    async def dj(self, ctx: SlashContext, **kwargs):
        pass

    @dj.subcommand(
        sub_cmd_name="v4",
        sub_cmd_description="DandJourney图像生成 For Version 4 版本",
        options=PromptCls.MultiplePrompt(BotSettings["BotParam"]["DJPrompt"]["Version4"]),
    )
    async def djv4(self, ctx: SlashContext, prompt:str, no:str = '', image:object = None, **kwargs):
        ChannelSwitch(ctx)
        _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"UV"})

        kwargs.update({"prompt": prompt, "no": no, "image": image, "QueueKey": _insert[0][1], "version": "4"})
        _PromptMix = PromptMix(**kwargs)
        prompt = _PromptMix.DJPromptMix()
        if prompt[0]:
            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.Imagine("<#{}> {}".format(_insert[0][1], prompt[1]), channel = _channel)
            if response[0]:
                await ctx.send("DandJourney接收参数:{}".format(prompt[1]))
            else:
                await ctx.send(response[1])
        else:
            SystemQueue.delete_queue_value(DQueueID, _insert[0][1])
            await ctx.send(prompt[1])

    @dj.subcommand(
        sub_cmd_name="v5",
        sub_cmd_description="DandJourney图像生成 For Version 5 版本",
        options=PromptCls.MultiplePrompt(BotSettings["BotParam"]["DJPrompt"]["Version5"]),
    )
    async def djv5(self, ctx: SlashContext, prompt:str, 
                   area:str = "", no:str = "", quality:float = None, stylize:int = None, niji:int = None, 
                   seed:int = None, chaos:int = None, image:object = None, imageratio:int = None, **kwargs):
        ChannelSwitch(ctx)
        _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"UV"})

        kwargs.update({"prompt": prompt, "area": area, "no": no, "quality": quality, "stylize": stylize, "niji": niji, 
                       "seed": seed, "chaos": chaos, "image": image, "imageratio": imageratio, "QueueKey": _insert[0][1], "version": "5"})
        _PromptMix = PromptMix(**kwargs)
        prompt = _PromptMix.DJPromptMix()
        if prompt[0]:
            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.Imagine("<#{}> {}".format(_insert[0][1], prompt[1]), channel = _channel)
            if response[0]:
                await ctx.send("DandJourney接收参数:{}".format(prompt[1]))
            else:
                await ctx.send(response[1])
        else:
            SystemQueue.delete_queue_value(DQueueID, _insert[0][1])
            await ctx.send(prompt[1])

    @dj.subcommand(
        sub_cmd_name="v5_1",
        sub_cmd_description="DandJourney图像生成 For Version 5.1 版本",
        options=PromptCls.MultiplePrompt(BotSettings["BotParam"]["DJPrompt"]["Version5.1"]),
    )
    async def djv51(self, ctx: SlashContext, prompt:str, 
                   area:str = "", no:str = "", style:bool = True, quality:float = None, stylize:int = None, niji:int = None, 
                   seed:int = None, chaos:int = None, image:object = None, imageratio:int = None, **kwargs):
        ChannelSwitch(ctx)
        _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"UV"})

        kwargs.update({"prompt": prompt, "area": area, "no": no, "quality": quality, "style": style, "stylize": stylize, "niji": niji, 
                       "seed": seed, "chaos": chaos, "image": image, "imageratio": imageratio, "QueueKey": _insert[0][1], "version": "5.1"})
        _PromptMix = PromptMix(**kwargs)
        prompt = _PromptMix.DJPromptMix()
        if prompt[0]:
            _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
            response = PostAgent.Imagine("<#{}> {}".format(_insert[0][1], prompt[1]), channel = _channel)
            if response[0]:
                await ctx.send("DandJourney接收参数:{}".format(prompt[1]))
            else:
                await ctx.send(response[1])
        else:
            SystemQueue.delete_queue_value(DQueueID, _insert[0][1])
            await ctx.send(prompt[1])

    @slash_command(name="dblend", description="DandJourney图像混合", options=PromptCls.MultiplePrompt(BotSettings["BotParam"]["DBlendPrompt"]))
    async def dblend(self, ctx: SlashContext,
                    image1: object, 
                    image2:object, 
                    image3:object = None, 
                    image4:object = None, 
                    image5:object = None, 
                    dimensions:str = "--ar 1:1",
                    **kwargs):
        ChannelSwitch(ctx)
        saveImg = await ctx.send("DandJourney正在转存图片...")

        _insert = SystemQueue.insert_queue(DQueueID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"UV"})
        _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id
        
        response = PostAgent.Blend([image1, image2, image3, image4, image5], dimensions, _insert[0][1], channel=_channel)
        if response[0]:
            await ctx.edit(message = saveImg.id, content = "DandJourney正在生成混合图片...")
        else:
            await ctx.edit(message = saveImg.id, content = response[1])

    @slash_command(name="ddescribe", description="DandJourney图像描述", options=PromptCls.SinglePrompt(BotSettings["BotParam"]["DDescribePrompt"]))
    async def ddescribe(self, ctx: SlashContext,
                    image: object, 
                    **kwargs):
        ChannelSwitch(ctx)
        saveImg = await ctx.send("DandJourney正在转存图片...")

        _insert = SystemQueue.insert_queue(DQueueFQID,{"User":ctx.author_id, "Channel":ctx.channel_id, "Mode":"DC", "Image": image.__getattribute__("url")})
        _channel = BotSettings["BotOpt"]["AGENT_CHANNEL"] if BotSettings["BotOpt"]["AGENT_SIGN"] else ctx.channel.id

        response = PostAgent.Describe(image, _insert[0][1], channel=_channel)
        if response[0]:
            await ctx.edit(message = saveImg.id, content = "DandJourney正在生成描述...")
        else:
            await ctx.edit(message = saveImg.id, content = response[1])


def setup(bot):
    print("Init BotCommand.py")
    BotCommandCls(bot)