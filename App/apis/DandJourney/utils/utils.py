import re
from . import agentBot, PostAgent, interactions, Banned_Word


# ********************************* Create Message ********************************* #
def CreateMsg(message):
    user = message.content.split("|")[-2]
    msg = message.referenced_message.content.split("**")[1]
    targetID = str(message.message_reference.message_id)
    targetHash = str((message.referenced_message.attachments[0].url.split("_")[-1]).split(".")[0])
    result = message.content.split("|")[-1]
    return "**{}的控制板**\n关键词：{}\nID：{}\nHash：{}\n生成图片：{}".format(user, msg, targetID, targetHash, result)


def CreateAgency(message, sign):
    user = re.findall("<@.*>", message.content)[0]
    imgURL = message.attachments[0].url
    return "Get Bot Message for {}|{}|{}".format(sign, user, imgURL)


def CreateAboutEmb():
    embed = interactions.Embed(title = "*****DandJourney*****", description = '用爱发电的消息转发机器人', color=0x00ff00, fontsize = 20)
    embed.add_field(name = '——'*15, value = "", inline = False)
    embed.add_field(name = '当前机器人名称', value = agentBot["BotInfo"]["Name"], inline = True)
    embed.add_field(name = '当前版本', value = agentBot["BotInfo"]["version"], inline = True)
    embed.set_footer(text = 'Made By Yuexdang Universe D Team', icon_url = 'https://user-images.githubusercontent.com/56034408/234861839-7cddd103-e597-4029-b514-063c4bca5227.png')
    embed.set_image(url='https://opengraph.githubassets.com/70433925c505ce837dda9bab06af0101f3ac5b592acc6763a52b04b9ef059142/yuexdang/DandJourney')
    return embed


def CreateHelpEmb():
    embed = interactions.Embed(title = "*****DandJourney*****", description = '用爱发电的消息转发机器人', color=0x00ff00, fontsize = 20)
    embed.add_field(name = '——'*6, value = "", inline = False)
    embed.add_field(name = 'DandJourney 指令集', value = "", inline = False)
    embed.add_field(name = '/dj `prompt` `*args`', value = "生成图片，附带版本下支持的所有参数", inline = False)
    embed.add_field(name = '/dblend `image(s)` `dim`', value = "混合图片，最多支持5张", inline = False)
    embed.add_field(name = '/dsettings', value = "打开控制面板，可调整版本等", inline = False)
    embed.add_field(name = '/aboutdj', value = "关于DandJourney", inline = False)
    embed.add_field(name = '/dhelp', value = "DandJourney的使用方法", inline = False)
    embed.set_footer(text = '更多请详见Usage.md文档')
    return embed

# ********************************* Options ********************************* #
def ChannelCheck(ctx):
    if agentBot["BotOpt"]["USE_CHANNEL"]:
        PostAgent.RefreshChannel(str(ctx.channel.id))
    return


# ********************************* Create Prompt ********************************* #
def PromptMix(prompt, area, quality, stylize, seed, chaos, image, imageratio):
    for __banned in Banned_Word:
        if __banned in prompt:
            return (False, "Has Banned Word:{}".format(__banned))
    try:
        if hasattr(image,'url') and "http" in image.url:
            prompt = prompt + " {} ".format(image.url)
    except Exception:
        return (False, "Error in PromptMix:{}".format(Exception))

    if (image or "http" in prompt) and imageratio:
        prompt = prompt + " --iw {} ".format(round(((imageratio + 5) * 0.1), 1))
        
    if quality and float(quality) > 0.25 and float(quality) < 2.0:
        prompt = prompt + " --quality {} ".format(quality)
    
    area_num = int(area.split(":")[0])/int(area.split(":")[1]) \
                if area and\
                    area.count(":") == 1 and \
                    len(area.split(":")) == 2 and \
                    all(_area.isdigit() for _area in area.split(":")) \
                else None

    if area_num and float(area_num) > 0.5 and float(area_num) < 2.0 and float(area_num) != 1.0:
        prompt = prompt + " --ar {} ".format(area)
    
    if seed and seed > 0 and seed < 4294967295:
        prompt = prompt + " --seed {} ".format(seed)
    
    if stylize and stylize > 0 and stylize < 1000:
        prompt = prompt + " --stylize {} ".format(stylize)

    if chaos:
        prompt = prompt + " --chaos {} ".format(chaos)

    prompt = prompt + " --v {} ".format(agentBot["BotInit"]["Version"][-1])
    
    return (True, prompt)