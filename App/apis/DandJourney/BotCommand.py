from . import bot, interactions, PostAgent, agentBot
from . import SettingButton, CreateMultipleButtons

from .utils.PromptChoice import dj, dblend, describe

from .utils.utils import ChannelCheck, PromptMix, CreateAboutEmb, CreateHelpEmb
from . import Button

def initCommand():
    print("Init BotCommand.py")


# *************************************************** slash 指令 *************************************************
# 第一个被初始化的不要有options，不然会出神奇的BUG（应该是时序的问题）

@bot.command(
    name = "dsettings",
    description = "DandJourney设置",
)
async def dj_settings(ctx: interactions.CommandContext):
    ChannelCheck(ctx)
    VersionComponent = CreateMultipleButtons(ButtonName = SettingButton, 
                                            custom_idDic={"V1":"Version1", "V2":"Version2", "V3":"Version3", "V4":"Version4", "V5":"Version5"}, 
                                            styleDic={"V"+agentBot["BotInit"]["Version"][-1]: 1, agentBot["BotInit"]["Speed"]: 1}, 
                                            disableDic={"V"+agentBot["BotInit"]["Version"][-1]: True, agentBot["BotInit"]["Speed"]: True}, 
                                            padding = [2,5], instantiation = True)
    VersionComponent = VersionComponent[1] if VersionComponent[0] else None
    await ctx.send(content = "机器人设置", components = VersionComponent)
    return


@bot.command(
    name = "dabout",
    description = "关于DandJourney",
)
async def dj_about(ctx: interactions.CommandContext):
    await ctx.send(embeds = CreateAboutEmb())
    return


@bot.command(
    name = "dhelp",
    description = "帮助手册",
)
async def dj_help(ctx: interactions.CommandContext):
    await ctx.send(embeds = CreateHelpEmb())
    return


@bot.command(
    name = "dj",
    description = "图像生成",
    options = dj
)
async def dj_imagine(ctx: interactions.CommandContext, 
                prompt: str, 
                area: str = None, 
                quality: str = None, 
                stylize: int = None, 
                seed: int = None, 
                chaos: int = None, 
                image = None, 
                imageratio: int = None):
    # 目前还没写动态变动变量，因为重新加载会消耗每日的命令创建次数
    ChannelCheck(ctx)
    prompt = PromptMix(prompt, area, quality, stylize, seed, chaos, image, imageratio)
    if prompt[0]:
        response = PostAgent.Imagine(prompt[1])
        if response[0]:
            await ctx.send("DandJourney接收参数:{}".format(prompt[1]))
        else:
            print(response[1])
    else:
        if "Banned" in prompt[1]:
            await ctx.send(prompt[1])
    return 


@bot.command(
    name = "dblend",
    description = "图像混合",
    options = dblend
)
async def dj_dblend(ctx: interactions.CommandContext,
                image1: object, 
                image2:object, 
                image3:object = None, 
                image4:object = None, 
                image5:object = None, 
                dimensions:str = "--ar 1:1"):
    
    # ChannelCheck(ctx)
    # response = PostAgent.Blend([image1, image2, image3, image4, image5], dimensions)
    # if response[0]:
    #     await ctx.send("丁真正在根据以下内容生成混合图片：图片组：{}，画面尺寸：{}".format([image1, image2, image3, image4, image5], dimensions))
    # else:
    #     print(response[1])
    await ctx.send('Blend is Coding...')
    return


@bot.command(
    name = "describe",
    description = "图像描述",
    options = describe
)
async def dj_describe(ctx: interactions.CommandContext,
                image: object):
    
    # ChannelCheck(ctx)
    # response = PostAgent.Describe(image)
    # if response[0]:
    #     await ctx.send("正在生成描述")
    # else:
    #     print(response[1])
    await ctx.send('Describe is Coding...')
    return






# ------------------------------------------------- #
initCommand()
# ------------------------------------------------- #