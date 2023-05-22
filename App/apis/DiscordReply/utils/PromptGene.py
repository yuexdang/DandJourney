from . import interactions, BotSettings

class PromptGenerate:
    """
    Discord选项生成器
    """
    def __typeChange(self, TypeIn: type) -> type:
        option_types = {
            "str": interactions.OptionType.STRING,
            "int": interactions.OptionType.INTEGER,
            "bool": interactions.OptionType.BOOLEAN,
            "User": interactions.OptionType.USER,
            "Member": interactions.OptionType.USER,
            "Channel": interactions.OptionType.CHANNEL,
            "Role": interactions.OptionType.ROLE,
            "float": interactions.OptionType.NUMBER,
            "Attachment": interactions.OptionType.ATTACHMENT,
        }
        return option_types.get(TypeIn, interactions.OptionType.STRING)

    def __ChoicePrompt(self, Choice: dict) -> list:
        return [interactions.SlashCommandChoice(name=choiceName, value=Choice[choiceName]) for choiceName in Choice]

    def __StaticPrompt(self, Prompt: dict) -> list:
        # 参数合规检验
        for needValue in ["name", "description", "type", "required"]:
            if needValue not in Prompt:
                raise ValueError("PromptError: Prompt'{}' is required".format(needValue))

        SlashOption = interactions.SlashCommandOption(
            name = Prompt["name"],
            description = Prompt["description"],
            type = self.__typeChange(Prompt["type"]),
            required = Prompt["required"],
        )

        if "choice" in Prompt:
            SlashOption.choices = self.__ChoicePrompt(Prompt["choice"])
        if "max" in Prompt:
            if Prompt["type"] == "str":
                SlashOption.max_length = Prompt["max"]
            if Prompt["type"] == "int" or Prompt["type"] == "float":
                SlashOption.max_value = Prompt["max"]
        if "min" in Prompt:
            if Prompt["type"] == "str":
                SlashOption.min_length = Prompt["min"]
            if Prompt["type"] == "int" or Prompt["type"] == "float":
                SlashOption.min_value = Prompt["min"]

        return SlashOption

    def SinglePrompt(self, Prompt: dict) -> list:
        return [self.__StaticPrompt(Prompt[0])]

    def MultiplePrompt(self, PromptList: list) -> list:
        return [self.__StaticPrompt(singlePrompt) for singlePrompt in PromptList]