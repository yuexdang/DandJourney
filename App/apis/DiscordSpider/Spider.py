import requests

from .utils.payload import JsonImagine, JsonFast, JsonRelax, JsonBlend, JsonMorph, JsonRegImg, JsonDescribe

from . import BotSettings


class PostMethod():
    """
    父类 PostMethod：
    该方法用于生成配置一些基础参数与基础方法
    该类可以自定义添加一些动态方法
    """
    def __init__(self, MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str, VIP_TOKEN : str) -> None:
        self.MID_JOURNEY_ID = MID_JOURNEY_ID
        self.SERVER_ID = SERVER_ID
        self.CHANNEL_ID = CHANNEL_ID
        
        self.header = {'authorization' : VIP_TOKEN}
        self.URL = "https://discord.com/api/v9/interactions"

        self.StorageURL = "https://discord.com/api/v9/channels/" + CHANNEL_ID + "/attachments"

    def __ResponseCheck(self, Response):
        """
        验证请求状态，类内方法
        """
        if Response.status_code >= 400:
            return (False, "ResponseError in Location:{}, Msg:{}, Code:{}".format("ResponseCheck" ,Response.text, Response.status_code))
        return (True, Response)

    def GetResponse(self, json : dict) -> bool:
        """
        验证请求状态，类外方法
        """
        try:
            response = requests.post(url = self.URL, json = json, headers = self.header)
            return self.__ResponseCheck(response)
        except Exception as e:
            return (False, "ResponseError in Location:{}, Msg:{}".format("GetResponse", e))

    def ImageStorage(self, ImageName : str, ImageUrl : str, ImageSize : int, prompt: str) -> tuple:
        """
        将Discord外链进行转存处理，并获取内链
        update 1: 支持添加所需要的参数,目前为JobID
        """
        try:
            ImageName = ImageName.split(".")
            ImageName = "{}_{}.{}".format(ImageName[0], prompt, ImageName[1])

            _response = requests.post(url = self.StorageURL, json = JsonRegImg(ImageName, ImageSize), headers = self.header)
            if self.__ResponseCheck(_response)[0]:
                __Res = _response.json()["attachments"][0]
                upload_url = __Res["upload_url"]
                upload_filename = __Res["upload_filename"]

                __response = requests.get(ImageUrl, headers={"authority":"cdn.discordapp.com"})
                if self.__ResponseCheck(__response)[0]:

                    ___response = requests.put(upload_url,data=__response.content, headers={"authority":"discord-attachments-uploads-prd.storage.googleapis.com"})
                    if self.__ResponseCheck(___response)[0]:
                        return (True, (ImageName, upload_filename))
                    else:
                        return (False, "StorageError in Location:ImageStorage, Msg:Can't Storage!")
                else:
                    return (False, "ReadError in Location:Image, Msg:Image is not exist!")
            else:
                return (False, "ResponseError in Location:GetResponse, Msg:Fail to get Response from Discord!")
        except Exception as e:
            return (False, "RunningError in Location:{}, Msg:{}".format("ImageStorage", e))

    def RefreshChannel(self, ChannelID : str) -> None:
        """
        刷新频道
        """
        self.CHANNEL_ID = ChannelID
        return


class DecoratorCls:
    """
    装饰器类：
    此类中存储所有需要的装饰器
    预留位置，暂时不用
    """
    def ChannelDC(self, func):
        def wrapper(innerSelf):
            pass
            func(innerSelf)
        return wrapper
    

class DiscordPost(PostMethod):
    DecoCls = DecoratorCls()
    def __init__(self) -> None:
        PostMethod.__init__(self, BotSettings["BotCode"]["MID_JOURNEY_ID"], BotSettings["BotCode"]["SERVER_ID"], BotSettings["BotCode"]["CHANNEL_ID"], BotSettings["BotCode"]["VIP_TOKEN"])
        pass

    def Imagine(self, prompt : str, channel : str = None) -> object:
        """
        用于图片生成
        """
        __payload = JsonImagine(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID, 
                                prompt)
        response = self.GetResponse(json = __payload)
        return response

    def Upscale(self, index : int, messageId : str, messageHash : str, channel : str = None):
        """
        用于图片放大 U按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "upsample")
        response = self.GetResponse(json = __payload)
        return response
    
    def Variation(self, index : int, messageId : str, messageHash : str, solo : bool = False, channel : str = None):
        """
        用于图片细分 V按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "variation", solo=solo)
        response = self.GetResponse(json = __payload)
        return response
    
    def Remaster(self, index : int, messageId : str, messageHash : str, channel : str = None):
        """
        用于大图细分 Remaster按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "remaster", solo = True)
        response = self.GetResponse(json = __payload)
        return response

    def LUpscale(self, index : int, messageId : str, messageHash : str, channel : str = None):
        """
        用于大图光影细分 Light Upscale Redo 按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "upsample_light", solo = True)
        response = self.GetResponse(json = __payload)
        return response

    def DUpscale(self, index : int, messageId : str, messageHash : str, channel : str = None):
        """
        用于大图细节细分 Detailed Upscale Redo 按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "upsample", solo = True)
        response = self.GetResponse(json = __payload)
        return response
    
    def BUpscale(self, index : int, messageId : str, messageHash : str, channel : str = None):
        """
        用于大图二阶细分 Beta Upscale Redo 按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "upsample_beta", solo = True)
        response = self.GetResponse(json = __payload)
        return response

    def Fast(self):
        """
        切换出图模式为:Fast
        """
        __payload = JsonFast(self.MID_JOURNEY_ID, self.SERVER_ID, self.CHANNEL_ID)
        response = self.GetResponse(json = __payload)
        return response
    
    def Relax(self):
        """
        切换出图模式为:Relax
        """
        __payload = JsonRelax(self.MID_JOURNEY_ID, self.SERVER_ID, self.CHANNEL_ID)
        response = self.GetResponse(json = __payload)
        return response

    def Blend(self, ImageSet : list, Dimensions : str, prompt : str, channel : str = None):
        """
        图片混合
        """
        __options , __attachments = [], []
        for Image in ImageSet:
            if Image:
                response = self.ImageStorage(ImageName = Image.__getattribute__("filename"), ImageUrl = Image.__getattribute__("url"), ImageSize = Image.__getattribute__("size"), prompt = prompt)
                if response[0]:
                    __options.append({"type":11,"name":"image{}".format(len(__options)+1),"value":len(__options)})
                    __attachments.append({"id":str(len(__options)-1),"filename":response[1][0],"uploaded_filename":response[1][1]})

        if Dimensions != "--ar 1:1":
            __options.insert(2,{"type":3,"name":"dimensions","value":Dimensions})

        __payload = JsonBlend(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID, 
                              __options, __attachments)
        response = self.GetResponse(json = __payload)
        return response
    
    def Refresh(self, index : int, messageId : str, messageHash : str, channel : str = None):
        """
        用于刷新图片
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                              index, messageId, messageHash, "reroll", solo=True)
        response = self.GetResponse(json = __payload)
        return response
    
    def Describe(self, Image : object, prompt : str, channel : str = None):
        """
        用于描述图片
        """
        response = self.ImageStorage(ImageName = Image.__getattribute__("filename"), ImageUrl = Image.__getattribute__("url"), ImageSize = Image.__getattribute__("size"), prompt = prompt)
        if response[0]:
            __attachments = [{"id":0, "filename":response[1][0],"uploaded_filename":response[1][1]}]

        __payload = JsonDescribe(self.MID_JOURNEY_ID, self.SERVER_ID, channel if channel else self.CHANNEL_ID,
                                  __attachments)
        response = self.GetResponse(json = __payload)
        return response
    
    def RegisterImage(self, filename : str, filesize : int, url : str):
        """
        注册图片，用于外链图片上传
        """
        __payload = JsonRegImg(filename, filesize, url)
        response = self.GetResponse(json = __payload)
        return response
