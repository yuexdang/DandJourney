# 记录一些消息的返回格式，如果需要自定义进行再创作可以从这里找参数

MessageReaction = """
MessageReaction(
    user_id=Snowflake(), 
    channel_id=Snowflake(), 
    message_id=Snowflake(), 
    guild_id=Snowflake(), 
    member=Member(
        user=User(
            id=Snowflake(), 
            username='', 
            discriminator='', 
            bot=False, mfa_enabled=None, locale=None, verified=None, email=None, bio=None
            ), 
        nick='',
        roles=[], deaf=False, mute=False, communication_disabled_until=None
    ), 
    emoji=Emoji(
        id=None, name='{}', roles=None, user=None, require_colons=None, managed=None, animated=None, available=None
    )
)
"""

Message = """
Message(
    id=Snowflake(), 
    channel_id=Snowflake(), 
    guild_id=Snowflake(), 
    author=User(
        id=Snowflake(), 
        username='', 
        discriminator='', 
        bot=None, mfa_enabled=None, locale=None, verified=None, email=None, bio=None
    ), 
    member=Member(
        user=User(
            id=Snowflake(), 
            username='', 
            discriminator='', 
            bot=None, mfa_enabled=None, locale=None, verified=None, email=None, bio=None
        ), 
        nick='', 
        roles=[], deaf=False, mute=False, communication_disabled_until=None
    ), 
    content='{}', 
    timestamp=datetime.datetime(), 
    edited_timestamp=None, tts=False, mention_everyone=False, mentions=[], mention_roles=[], 
    mention_channels=None, attachments=[], embeds=[], reactions=None, pinned=False, webhook_id=None, 
    type=<MessageType.DEFAULT: 0>, activity=None, application=None, application_id=None, 
    message_reference=None, flags=<MessageFlags.0: 0>, referenced_message=None, thread=None, 
    components=[], sticker_items=None, stickers=None
)"""

Message_Midjourney_CreateImg = """
Message(
    id=Snowflake(), 
    channel_id=Snowflake(), 
    guild_id=Snowflake(), 
    author=User(
        id=Snowflake(), 
        username='Midjourney Bot', 
        discriminator='', 
        bot=True, mfa_enabled=None, locale=None, verified=None, email=None, bio=None
    ), 
    member=Member(
        user=User(
            id=Snowflake(), 
            username='Midjourney Bot', 
            discriminator='', 
            bot=True, mfa_enabled=None, locale=None, verified=None, email=None, bio=None
        ), 
        nick=None, roles=[], deaf=False, mute=False, communication_disabled_until=None
    ), 
    content='', 
    timestamp=datetime.datetime(), 
    edited_timestamp=None, tts=False, mention_everyone=False, 
    mentions=[
        {
            'username': '', 'public_flags': 0, 
            'member': {
                'roles': [''], 
                'premium_since': None, 'pending': False, 'nick': None, 'mute': False, 
                'joined_at': '', 'flags': 0, 'deaf': False, 
                'communication_disabled_until': None, 'avatar': None
            }, 
            'id': '', 
            'global_name': None, 'display_name': None, 'discriminator': '', 
            'avatar_decoration': None, 'avatar': ''
        }
    ], 
    mention_roles=[], mention_channels=None, 
    attachments=[
        Attachment(
            id=Snowflake(), 
            filename='', 
            content_type='image/png', size=, 
            url='';, 
            proxy_url='';, 
            height=, width=, ephemeral=None
        )
    ], 
    embeds=[], reactions=None, pinned=False, webhook_id=None, type=<MessageType.DEFAULT: 0>, activity=None, application=None, application_id=None, message_reference=None, 
    flags=<MessageFlags.0: 0>, referenced_message=None, thread=None, 
    components=[
        ActionRow(
            type=<ComponentType.ACTION_ROW: 1>, 
            components=[
                Component(
                    type=<ComponentType.BUTTON: 2>, 
                    custom_id='', 
                    disabled=None, style=<ButtonStyle.SECONDARY: 2>, label='U1', emoji=None, url=None, 
                    options=None, placeholder=None, min_values=None, max_values=None, components=None, min_length=None, max_length=None, required=None, value=None
                ), 
            ]
        ), 
        ActionRow(
            type=<ComponentType.ACTION_ROW: 1>, 
            components=[
                Component(
                    type=<ComponentType.BUTTON: 2>, 
                    custom_id='', 
                    disabled=None, style=<ButtonStyle.SECONDARY: 2>, label='V1', emoji=None, url=None, 
                    options=None, placeholder=None, min_values=None, max_values=None, components=None, min_length=None, max_length=None, required=None, value=None
                ), 
            ]
        )
    ], 
    sticker_items=None, stickers=None
)
"""