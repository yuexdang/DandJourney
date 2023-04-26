import interactions
from interactions import Button, SelectMenu, SelectOption, spread_to_rows

from .. import Settings as agentBot
from .. import Banned_Word, DjPromptDic

from ..DiscordSpider import PostAgent

bot = interactions.Client(
                token=agentBot["BotCode"]["BOT_TOKEN"],
                default_scope=agentBot["BotCode"]["SERVER_ID"],
                intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT,
            )

from .InitStaticComponent import CreateMultipleButtons
from .InitStaticComponent import UVComponent, SettingButton, MakeVComponent
