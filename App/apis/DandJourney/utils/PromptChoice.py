from . import interactions, agentBot, DjPromptDic


def DjInit(Version: str) -> list:
    # 生成DJ参数（随Version变动）
    __tempList = []
    for __prompt in DjPromptDic[Version]:
        __promptObj = interactions.Option(
            name = __prompt["name"],
            description = __prompt["description"]+" [{}]".format(Version),
            type = interactions.OptionType.INTEGER if __prompt["type"] is int else interactions.OptionType.STRING if __prompt["type"] is str else interactions.OptionType.ATTACHMENT,
            required = __prompt["required"],
        )
        if "max" in __prompt and "min" in __prompt:
            __promptObj.max_value = __prompt["max"]
            __promptObj.min_value = __prompt["min"]
        __tempList.append(__promptObj)
    return __tempList


dj = DjInit(agentBot["BotInit"]["Version"])

dblend = [
    interactions.Option(
        name="image1",
        description="图图",
        type=interactions.OptionType.ATTACHMENT,
        required=True,
    ),
    interactions.Option(
        name="image2",
        description="图图",
        type=interactions.OptionType.ATTACHMENT,
        required=True,
    ),
    interactions.Option(
        name="dimensions",
        description="图像尺寸",
        type=interactions.OptionType.STRING,
        required=False,
        choices = [
            interactions.Choice(name="2：3 → 半身", value="--ar 2:3"),
            interactions.Choice(name="1：1 → 矩形", value="--ar 1:1"),
            interactions.Choice(name="3：2 → 广角", value="--ar 3:2"),
        ],
    ),
    interactions.Option(
        name="image3",
        description="图图",
        type=interactions.OptionType.ATTACHMENT,
        required=False,
    ),
    interactions.Option(
        name="image4",
        description="图图",
        type=interactions.OptionType.ATTACHMENT,
        required=False,
    ),
    interactions.Option(
        name="image5",
        description="图图",
        type=interactions.OptionType.ATTACHMENT,
        required=False,
    ),
]

describe = [
    interactions.Option(
        name="image",
        description="图图",
        type=interactions.OptionType.ATTACHMENT,
        required=True,
    ),
]