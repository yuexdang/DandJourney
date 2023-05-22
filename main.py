from App import BotAgent

if __name__ == '__main__':
    from interactions.client import const
    const.CLIENT_FEATURE_FLAGS["FOLLOWUP_INTERACTIONS_FOR_IMAGES"] = True
    BotAgent.start()