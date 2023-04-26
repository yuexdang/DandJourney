import re

from . import bot, interactions, PostAgent, agentBot

from .utils.component import ButtonClick


def initCommand():
    print("Init BotComponent.py")


# *************************************************** 批量功能初始化 *************************************************
def UVEditorGenerate(UVlist):
    # 动态生成 UV 对应方法
    for UV in UVlist:
        UVeditor = """\
@bot.component('{sign}')
async def UVEditor{sign}(ctx: interactions.CommandContext):
    targetID, targetHash = re.findall(r"ID：.*\\n",ctx.message.content)[0][3:-1], re.findall(r"Hash：.*\\n",ctx.message.content)[0][5:-1]
    response = PostAgent.{refer}( str(ctx.channel.id), '{sign}'[1], targetID, targetHash)
    if response[0]:
        await ctx.edit(components = ButtonClick(ctx))
        await ctx.send('正在进行操作：{sign}细分', ephemeral=True)
    else:
        print(response[1])
    return
        """.format(sign = UV, refer = "Upscale" if "U" in UV else "Variation")
        exec(UVeditor)

def VersionGenerate(versions):
    # 动态生成 Version 对应方法
    for version in versions:
        VersionEditor = """\
@bot.component('{sign}')
async def Editor{sign}(ctx: interactions.CommandContext):

    await ctx.edit(components = ButtonClick(ctx, Switch=["BotInit", "Version"]))
    agentBot["BotInit"]["Version"] = '{sign}'
    await ctx.send('设置MidJourney版本为:{sign}', ephemeral=True)
        """.format(sign = version)
        exec(VersionEditor)


# *************************************************** 特殊功能初始化 *************************************************
@bot.component('Refresh')
async def tester(ctx: interactions.CommandContext):
    # 拓展生成
    targetID, targetHash = re.findall(r"ID：.*\n",ctx.message.content)[0][3:-1], re.findall(r"Hash：.*\n",ctx.message.content)[0][5:-1]
    response = PostAgent.Refresh(str(ctx.channel.id), 0, targetID, targetHash)
    if response[0]:
        await ctx.edit(components = ButtonClick(ctx, disable = False))
        await ctx.send('正在重新生成照片', ephemeral=True)
    else:
        print(response[1])
    return


@bot.component('BlendG')
async def tester(ctx: interactions.CommandContext):
    # 混合所有的图(能不能做还不一定,说不定哪一天就给这个功能删了)
    await ctx.send('Blend Image Group is Coding...')


@bot.component('Fast')
async def tester(ctx: interactions.CommandContext):
    # 调整模式为：Fast
    response = PostAgent.Fast()
    if response[0]:
        await ctx.edit(components = ButtonClick(ctx, Switch=["BotInit", "Speed"]))
        agentBot["BotInit"]["Speed"] = "Fast"
        await ctx.send('模式切换至:Fast')
    else:
        print(response[1])
    return


@bot.component('Relax')
async def tester(ctx: interactions.CommandContext):
    # 调整模式为：Relax
    response = PostAgent.Relax()
    if response[0]:
        await ctx.edit(components = ButtonClick(ctx, Switch=["BotInit", "Speed"]))
        agentBot["BotInit"]["Speed"] = "Relax"
        await ctx.send('模式切换至:Relax')
    else:
        print(response[1])
    return


@bot.component('DescribeU')
async def tester(ctx: interactions.CommandContext):
    # 描述通过U生成的图片
    await ctx.send('Describe The Image You Generated is Coding...')


@bot.component('VariationU')
async def tester(ctx: interactions.CommandContext):
    # 细分通过U生成的图片
    targetID, targetHash = re.findall(r"ID：.*\n",ctx.message.content)[0][3:-1], re.findall(r"Hash：.*\n",ctx.message.content)[0][5:-1]
    response = PostAgent.Variation(str(ctx.channel.id), 1, targetID, targetHash, solo=True)
    if response[0]:
        await ctx.edit(components = ButtonClick(ctx, disable = False))
        await ctx.send('正在细分生成照片', ephemeral=True)
    else:
        print(response[1])
    return




# ------------------------------------------------- #
initCommand()
# ------------------------------------------------- #
