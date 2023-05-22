# Channel Method

from . import BotSettings, PostAgent

"""
Channel Method Group:
这里放置所有的与频道操作有关的内容
包含频道切换,频道隔离等功能
"""

# Switch Channel
def ChannelSwitch(ctx):
    if BotSettings["BotOpt"]["USE_CHANNEL"]:
        PostAgent.RefreshChannel(str(ctx.channel.id))

# Isolation Channel