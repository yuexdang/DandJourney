import re

from .config import BOT_TOKEN, SERVER_ID, VIP_TOKEN, CHANNEL_ID, USE_MESSAGED_CHANNEL, MID_JOURNEY_ID, PROXY_CHANNEL, HAS_RUN, BOT_NAME
# 关于权限名单功能，后期会逐步弃用，改为数据库记录
from .config import AUTHORITY_LIST

def ConfigCheck(Config):
    if bool(re.findall("^_Add.*HERE_$", Config)):
        raise ValueError("初始变量{}未定义".format(Config))
    return Config


Settings = {
    "BotCode" : {
        "BOT_TOKEN": ConfigCheck(BOT_TOKEN),
        "SERVER_ID": ConfigCheck(SERVER_ID),
        "VIP_TOKEN": ConfigCheck(VIP_TOKEN),
        "CHANNEL_ID": ConfigCheck(CHANNEL_ID),
        "MID_JOURNEY_ID": MID_JOURNEY_ID,
    },
    "BotOpt" : {
        "USE_CHANNEL": USE_MESSAGED_CHANNEL,
        "USE_PROXY_CHANNEL": bool(PROXY_CHANNEL),
        "PROXY_CHANNEL": PROXY_CHANNEL,
        "HAS_RUN": HAS_RUN
    },
    "BotInfo" : {
        "Name": BOT_NAME,
        "version": "v2.0.0P",
    },
    "BotInit" : {
        "Version": "Version5",
        "Speed": "Fast",
    },
}

Banned_Word = ["blood"]

DjPromptDic = {
    "Version1":[
        {"name": "prompt", "description": "图片参数", "type": str, "required": True},
    ],
    "Version2":[
        {"name": "prompt", "description": "图片参数", "type": str, "required": True},
    ],
    "Version3":[
        {"name": "prompt", "description": "图片参数", "type": str, "required": True},
    ],
    "Version4":[
        {"name": "prompt", "description": "图片参数", "type": str, "required": True},
    ],
    "Version5":[
        {"name": "prompt", "description": "图片参数", "type": str, "required": True},
        {"name": "area", "description": "图像比例(1:2-2:1)", "type": str, "required": False},
        {"name": "quality", "description": "图像质量(0.25-2.0)", "type": str, "required": False},
        {"name": "stylize", "description": "风格化参数(0-1000)", "type": int, "required": False, "max": 1000, "min": 0},
        {"name": "seed", "description": "图像种子", "type": int, "required": False, "max":4294967295, "min": 0},
        {"name": "chaos", "description": "图像差异值", "type": int, "required": False, "max":100, "min": 0},
        {"name": "image", "description": "参考图像", "type": object, "required": False},
        {"name": "imageratio", "description": "参考图像权重", "type": int, "required": False, "max":15, "min": 0},
    ],
}