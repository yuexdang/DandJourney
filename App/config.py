import os

VenvValue = os.environ

# 环境需要插入的变量:
VenvNeed = ["BOT_TOKEN", "SERVER_ID", "VIP_TOKEN", "CHANNEL_ID", "CHANNEL_SIGN", "PROXY_CHANNEL", "MID_JOURNEY_ID"]

#strings 格式

BOT_TOKEN = VenvValue.get('BOT_TOKEN') if "BOT_TOKEN" in VenvValue else "_Add your BOT_TOKEN HERE_"
BOT_NAME = VenvValue.get('BOT_NAME') if "BOT_NAME" in VenvValue else "_Add your BOT_NAME HERE_"

SERVER_ID = VenvValue.get('SERVER_ID') if "SERVER_ID" in VenvValue else "_Add your SERVER_ID HERE_"
VIP_TOKEN = VenvValue.get('VIP_TOKEN') if "VIP_TOKEN" in VenvValue else "_Add your VIP_TOKEN HERE_"
CHANNEL_ID = VenvValue.get('CHANNEL_ID') if "CHANNEL_ID" in VenvValue else "_Add your CHANNEL_ID HERE_" 

# 是否启用代理频道 此频道用于MJ发送消息 若启用flask则此项为必填项
AGENT_CHANNEL = VenvValue.get('AGENT_CHANNEL') if "AGENT_CHANNEL" in VenvValue else None

# 是否启用代理服务 URL为本地代理链接 AUTH为认证账号与密码:Tuple(user, pwd)
PROXY_URL = VenvValue.get('PROXY_URL') if "PROXY_URL" in VenvValue else None

#tuple 格式
PROXY_AUTH = VenvValue.get('PROXY_AUTH') if "PROXY_AUTH" in VenvValue else None

#boolean 格式
# 这个已经彻底没用了 需要设置的话请在discord上面设置
USE_MESSAGED_CHANNEL = True if "CHANNEL_SIGN" in VenvValue and VenvValue.get('CHANNEL_SIGN') == "True" else False 

#list 格式

AUTHORITY_LIST = []

# 初始化属性 不需要改动

HAS_RUN = False
MID_JOURNEY_ID = VenvValue.get('MID_JOURNEY_ID') if "MID_JOURNEY_ID" in VenvValue else "936929561302675456"  #midjourney bot id
