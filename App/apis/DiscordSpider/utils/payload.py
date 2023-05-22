from .Globals import Imagine as ImaginePrompt
from .Globals import Morph as MorphPrompt
from .Globals import Fast as FastPrompt
from .Globals import Relax as RelaxPrompt
from .Globals import Blend as BlendPrompt
from .Globals import Describe as DescribePrompt


def JsonImagine(MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str, prompt : str) -> dict:
    """
    Imagine 方法请求参数生成
    """
    __payload = {
        "type":2,
        "application_id": MID_JOURNEY_ID,
        "guild_id": SERVER_ID,
        "channel_id": CHANNEL_ID,
        "session_id":ImaginePrompt["session_id"],
        "data":{
                "version" : ImaginePrompt["version"],
                "id" : ImaginePrompt["id"],
                "name":"imagine","type":1,
                "options":[
                            {
                                "type":3,"name":"prompt",
                                "value":prompt
                            }
                    ],
                "application_command":{
                                        "id":ImaginePrompt["id"],
                                        "application_id":MID_JOURNEY_ID,
                                        "version":ImaginePrompt["version"], 
                                        "default_permission":True, "default_member_permissions":None,"type":1,"nsfw":False,"name":"imagine",
                                        "description":"Create images with Midjourney","dm_permission":True,
                                        "options":[{"type":3,"name":"prompt","description":"The prompt to imagine","required":True}]
                                        },
                "attachments":[]
        }
    }
    return __payload

def JsonMorph(MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str, index : int, messageId : str, messageHash : str, morph : str, solo : bool = False) -> dict:
    """
    PicMorph 方法请求参数生成
    包含 upsample、variation、reroll 三种方法
    """
    __payload = {
        "type":3,
        "guild_id":SERVER_ID,
        "channel_id":CHANNEL_ID,
        "message_flags":0,
        "message_id": messageId,
        "application_id":MID_JOURNEY_ID,
        "session_id":MorphPrompt[morph],
        "data":{
                "component_type":2,
                "custom_id":"MJ::JOB::{}::{}::{}{}".format(morph, index, messageHash, "::SOLO" if solo else "")
        }
    }  
    return __payload


def JsonFast(MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str):
    """
    Fast 方法请求参数生成
    """
    __payload = {
        "type":2,
        "application_id":MID_JOURNEY_ID,
        "guild_id":SERVER_ID,
        "channel_id":CHANNEL_ID,
        "session_id":FastPrompt["session_id"],
        "data":{
            "version":FastPrompt["version"],
            "id":FastPrompt["id"],
            "name":"fast","type":1,"options":[],
            "application_command":{
                "id":FastPrompt["id"],
                "application_id":MID_JOURNEY_ID,
                "version":FastPrompt["version"],
                "default_permission":True,"default_member_permissions":None,"type":1,"nsfw":False,
                "name":"fast","description":"Switch to fast mode","dm_permission":True
                },"attachments":[]
        }
    }
    return __payload


def JsonRelax(MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str) -> dict:
    """
    Relax 方法请求参数生成
    """
    __payload = {
        "type":2,
        "application_id":MID_JOURNEY_ID,
        "guild_id":SERVER_ID,
        "channel_id":CHANNEL_ID,
        "session_id":RelaxPrompt["session_id"],
        "data":{
            "version":RelaxPrompt["version"],
            "id":RelaxPrompt["id"],
            "name":"relax","type":1,"options":[],
            "application_command":{
                "id":RelaxPrompt["id"],
                "application_id":MID_JOURNEY_ID,
                "version":RelaxPrompt["version"],
                "default_permission":True,"default_member_permissions":None,"type":1,"nsfw":False,
                "name":"relax","description":"Switch to relax mode","dm_permission":True
                },"attachments":[]
        }
    }
    return __payload


def JsonRegImg(filename : str, filesize : int) -> dict:
    """
    图片转存 请求参数生成
    """
    __payload = {"files": [{"filename": filename, "file_size": filesize, "id": 0}]}
    return __payload


def JsonBlend(MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str, options : list, attachments : list) -> dict:
    """
    Blend 方法请求参数生成
    """
    __payload = {
        "type":2,
        "application_id":MID_JOURNEY_ID,
        "guild_id":SERVER_ID,
        "channel_id":CHANNEL_ID,
        "session_id":BlendPrompt["session_id"],
        "data":{
            "version":BlendPrompt["version"],
            "id":BlendPrompt["id"],
            "name":"blend","type":1,"options":options,
            "application_command":{
                "id":BlendPrompt["id"],
                "application_id":MID_JOURNEY_ID,
                "version":BlendPrompt["version"],
                "default_member_permissions":None,"type":1,"nsfw":False,
                "name":"blend","description":"Blend images together seamlessly!","dm_permission":True,"contexts":None,
                "options":[
                    {"type":11,"name":"image1","description":"First image to add to the blend","required":True},
                    {"type":11,"name":"image2","description":"Second image to add to the blend","required":True},
                    {"type":3,"name":"dimensions","description":"The dimensions of the image. If not specified, the image will be square.","choices":[{"name":"Portrait","value":"--ar 2:3"},{"name":"Square","value":"--ar 1:1"},{"name":"Landscape","value":"--ar 3:2"}]},
                    {"type":11,"name":"image3","description":"Third image to add to the blend (optional)"},
                    {"type":11,"name":"image4","description":"Fourth image to add to the blend (optional)"},
                    {"type":11,"name":"image5","description":"Fifth image to add to the blend (optional)"}
                ]
            },"attachments":attachments,
        }
    }
    return __payload


def JsonDescribe(MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str, attachments : list) -> dict:
    """
    Describe 方法请求参数生成
    """
    __payload = {
        "type":2,
        "application_id":MID_JOURNEY_ID,
        "guild_id":SERVER_ID,
        "channel_id":CHANNEL_ID,
        "session_id":DescribePrompt["session_id"],
        "data":{
            "version":DescribePrompt["version"],
            "id":DescribePrompt["id"],
            "name":"describe","type":1,"options":[{"type":11,"name":"image","value":0}],
            "application_command":{
                "id":DescribePrompt["id"],
                "application_id":MID_JOURNEY_ID,
                "version":DescribePrompt["version"],
                "default_member_permissions":None,"type":1,"nsfw":False,"name":"describe",
                "description":"Writes a prompt based on your image.","dm_permission":True,"contexts":None,
                "options":[{"type":11,"name":"image","description":"The image to describe","required":True}]
            },"attachments":attachments
        }
    }
    return __payload