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

PROXY_CHANNEL = VenvValue.get('PROXY_CHANNEL') if "PROXY_CHANNEL" in VenvValue else None

#boolean 格式

USE_MESSAGED_CHANNEL = True if "CHANNEL_SIGN" in VenvValue and VenvValue.get('CHANNEL_SIGN') == "True" else False 

#list 格式

AUTHORITY_LIST = []

# 初始化属性 不需要改动

HAS_RUN = False
MID_JOURNEY_ID = "936929561302675456"  #midjourney bot id
