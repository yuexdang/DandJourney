from . import interactions, BotSettings

import re

def AboutEmb():
    embed = interactions.Embed(title = "*****DandJourney*****", description = '用爱发电的消息转发机器人', color=0x00ff00, url='https://github.com/yuexdang/DandJourney',
                               images=[interactions.EmbedAttachment(url="https://opengraph.githubassets.com/70433925c505ce837dda9bab06af0101f3ac5b592acc6763a52b04b9ef059142/yuexdang/DandJourney")])
    embed.set_image('https://opengraph.githubassets.com/70433925c505ce837dda9bab06af0101f3ac5b592acc6763a52b04b9ef059142/yuexdang/DandJourney')
    embed.add_field(name = '——'*15, value = " ", inline = False)
    embed.add_field(name = '当前机器人名称', value = BotSettings["BotInfo"]["Name"], inline = True)
    embed.add_field(name = '当前版本', value = BotSettings["BotInfo"]["version"], inline = True)
    embed.set_footer(text = 'Made By Yuexdang Universe D Team', icon_url = 'https://user-images.githubusercontent.com/56034408/234861839-7cddd103-e597-4029-b514-063c4bca5227.png')
    return embed

def HelpEmb():
    embed = interactions.Embed(title = "*****DandJourney*****", description = '用爱发电的消息转发机器人', color=0x00ff00)
    embed.add_field(name = '——'*6, value = " ", inline = False)
    embed.add_field(name = 'DandJourney 指令集', value = " ", inline = True)
    embed.add_field(name = '/dj `prompt` `*args`', value = "生成图片，附带版本下支持的所有参数", inline = False)
    embed.add_field(name = '/ddescribe `image`', value = "描述图片", inline = False)
    embed.add_field(name = '/dblend `image(s)` `dim`', value = "混合图片，最多支持5张", inline = False)
    embed.add_field(name = '/dsettings', value = "打开控制面板", inline = False)
    embed.add_field(name = '/aboutdj', value = "关于DandJourney", inline = False)
    embed.add_field(name = '/dhelp', value = "DandJourney的使用方法", inline = False)
    embed.set_footer(text = '更多请详见Usage.md文档')
    return embed

def ImageEmb(message):
    mode, user, result, channel, jobID, msgJobID = message.content.split("|")[-6:]
    msg = re.sub(r'<(?!https?:\/\/\S+).*?>|\*', '', message.get_referenced_message().content)
    targetID = str(message.message_reference.message_id)
    targetHash = str((message.get_referenced_message().attachments[0].url.split("_")[-1]).split(".")[0])

    embed = interactions.Embed(title = "***DandJourney图像板***", description = ' ', color=0x3eede7)
    embed.add_field(name = '关键词:', value = msg, inline = False)
    embed.add_field(name = 'TargetID', value = targetID, inline = False)
    embed.add_field(name = 'TargetHash', value = targetHash, inline = False)
    embed.add_field(name = 'JobID', value = jobID if "BT" not in mode else jobID.split("#")[0], inline = False)
    embed.set_image(result)
    return mode, user, embed, channel, jobID, msgJobID

def DescribeEmb(description, image):
    embed = interactions.Embed(title = "***DandJourney描述板***", description = description, color=0x3eede7)
    embed.set_image(image)
    return embed