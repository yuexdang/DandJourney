import interactions
from interactions import Button

from .. import BotSettings
from .. import Banned_Word, DjPromptDic
from .. import SystemQueue, DQueueID, DQueueFQID

from ..DiscordSpider import PostAgent

BotAgent = interactions.Client(
                token=BotSettings["BotCode"]["BOT_TOKEN"],
                default_scope=BotSettings["BotCode"]["SERVER_ID"],
                intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES | interactions.Intents.MESSAGE_CONTENT ,
                proxy_url=BotSettings["BotOpt"]["PROXY_URL"],
                proxy_auth=BotSettings["BotOpt"]["PROXY_AUTH"],
            )


BotAgent.load_extension("App.apis.DiscordReply.BotCommand")
BotAgent.load_extension("App.apis.DiscordReply.BotComponent")
BotAgent.load_extension("App.apis.DiscordReply.BotEvent")