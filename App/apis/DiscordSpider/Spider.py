import requests

from .utils.payload import JsonImagine, JsonFast, JsonRelax, JsonBlend, JsonMorph
from .utils.formatters import BlendFormat

from . import agentBot


class PostMethod():
    
    def __init__(self, MID_JOURNEY_ID : str, SERVER_ID : str, CHANNEL_ID : str, VIP_TOKEN : str) -> None:
        self.MID_JOURNEY_ID = MID_JOURNEY_ID
        self.SERVER_ID = SERVER_ID
        self.CHANNEL_ID = CHANNEL_ID
        
        self.header = {'authorization' : VIP_TOKEN}
        self.URL = "https://discord.com/api/v9/interactions"

    def __ResponseCheck(self, Response):
        if Response.status_code >= 400:
            print("Error in ResponseCheck: Msg:{},Code:{}".format(Response.text, Response.status_code))
            return (False, "Error! Msg:{},Code:{}".format(Response.text, Response.status_code))
        return (True, Response)

    def GetResponse(self, json : dict) -> bool:
        try:
            response = requests.post(url = self.URL, json = json, headers = self.header)
            return self.__ResponseCheck(response)
        except Exception as e:
            print("Error in GetResponse:{}".format(e))
            return (False, e)

    def RefreshChannel(self, ChannelID : str) -> None:
        self.CHANNEL_ID = ChannelID
        return


class DiscordPost(PostMethod):

    def __init__(self, Bots : dict) -> None:
        PostMethod.__init__(self, Bots["MID_JOURNEY_ID"], Bots["SERVER_ID"], Bots["CHANNEL_ID"], Bots["VIP_TOKEN"])
        pass

    def Imagine(self, prompt : str) -> object:
        """
        用于图片生成
        """
        __payload = JsonImagine(self.MID_JOURNEY_ID, self.SERVER_ID, self.CHANNEL_ID, prompt)
        response = self.GetResponse(json = __payload)
        return response

    def Upscale(self, channel : int, index : int, messageId : str, messageHash : str):
        """
        用于图片放大 U按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if agentBot["BotOpt"]["USE_CHANNEL"] else self.CHANNEL_ID, index, messageId, messageHash, "upsample")
        response = self.GetResponse(json = __payload)
        return response
    
    def Variation(self, channel : int, index : int, messageId : str, messageHash : str, solo : bool = False):
        """
        用于图片细分 V按钮
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if agentBot["BotOpt"]["USE_CHANNEL"] else self.CHANNEL_ID, index, messageId, messageHash, "variation", solo=solo)
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
    
    def Blend(self, ImageSet : list, Dimensions : str):
        """
        图片混合
        """
        __result = BlendFormat(ImageSet, Dimensions)
        if __result[0]:
            [__options, __attachments] = __result[1]
        else:
            return __result[1]
        __payload = JsonBlend(self.MID_JOURNEY_ID, self.SERVER_ID, self.CHANNEL_ID, __options, __attachments)
        response = self.GetResponse(json = __payload)
        return response
    
    def Refresh(self, channel : int, index : int, messageId : str, messageHash : str):
        """
        用于刷新图片
        """
        __payload = JsonMorph(self.MID_JOURNEY_ID, self.SERVER_ID, channel if agentBot["BotOpt"]["USE_CHANNEL"] else self.CHANNEL_ID, index, messageId, messageHash, "reroll", solo=True)
        response = self.GetResponse(json = __payload)
        return response
