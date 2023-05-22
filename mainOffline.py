import os

# 必要参数
os.environ['BOT_TOKEN'] = ""
os.environ['BOT_NAME'] = ""
os.environ['SERVER_ID'] = ""
os.environ['VIP_TOKEN'] = ""
os.environ['CHANNEL_ID'] = ""

# 可选参数,按需添加

# 机器人消息更新是否跟随频道变化
os.environ["CHANNEL_SIGN"] = "True"

#是否使用代理 
os.environ["PROXY_URL"] = ""

# MJ消息是否汇总于指定频道
os.environ["AGENT_CHANNEL"] = ""


from App import BotAgent

if __name__ == '__main__':
    from interactions.client import const
    const.CLIENT_FEATURE_FLAGS["FOLLOWUP_INTERACTIONS_FOR_IMAGES"] = True
    BotAgent.start()