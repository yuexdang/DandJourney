Banned_Word = [
      "blood", "bloodbath", "crucifixion", "bloody", "flesh", "bruises", "car crash", "corpse", "crucified", "cutting", "decapitate", "infested", "gruesome", "kill", "infected", "sadist", "slaughter", "teratoma", "tryphophobia", "wound", "cronenberg", "khorne", "cannibal", "cannibalism", "visceral", "guts", "bloodshot", "gory", "killing", "surgery", "vivisection", "massacre", "hemoglobin", "suicide",
      "ahegao", "pinup", "ballgag", "playboy", "bimbo", "pleasure", "bodily fluids", "pleasures", "boudoir", "rule34", "brothel", "seducing", "dominatrix", "seductive", "erotic", "fuck", "sensual", "hardcore", "sexy", "hentai", "shag", "horny", "shibari", "incest", "smut", "jav", "succubus", "jerk off king at pic", "thot", "kinbaku", "transparent", "legs spread", "twerk", "making love", "voluptuous", "naughty", "wincest", "orgy", "sultry", "xxx", "bondage", "bdsm", "dog collar", "slavegirl", "transparent", "translucent",
      "arse", "labia", "ass", "mammaries", "badonkers", "minge", "big ass", "mommy milker", "booba", "nipple", "booty", "oppai", "bosom", "organs", "breasts", "ovaries", "busty", "penis", "clunge", "phallus", "crotch", "sexy female", "dick", "skimpy", "girth", "thick", "honkers", "vagina", "hooters", "veiny", "knob",
      "no clothes", "au naturale", "no shirt", "bare chest", "nude", "barely dressed", "bra", "risqué", "clear", "scantily", "clad", "cleavage", "stripped", "full frontal", "unclothed", "invisible clothes", "wearing nothing", "lingerie", "with no shirt", "naked", "without clothes on", "negligee", "zero clothes",
      "taboo", "fascist", "nazi", "prophet mohammed", "slave", "coon", "honkey",
      "drugs", "cocaine", "heroin", "meth", "crack",
      "torture", "disturbing", "farts", "fart", "poop", "warts", "shit", "brown pudding", "bunghole", "vomit", "voluptuous", "seductive", "sperm", "hot", "sexy", "sensored", "censored", "silenced", "deepfake", "inappropriate", "pus", "waifu", "mp5", "succubus", "1488", "surgery"
    ]

DjPromptDic = {
    "Version1":[
        {"name": "prompt", "description": "图片参数", "type": "str", "required": True},
    ],
    "Version2":[
        {"name": "prompt", "description": "图片参数", "type": "str", "required": True},
    ],
    "Version3":[
        {"name": "prompt", "description": "图片参数", "type": "str", "required": True},
    ],
    "Version4":[
        {"name": "prompt", "description": "图片参数", "type": "str", "required": True},
        {"name": "no", "description": "屏蔽词汇", "type": "str", "required": False},
        {"name": "image", "description": "参考图像", "type": "Attachment", "required": False},
    ],
    "Version5":[
        {"name": "prompt", "description": "图片参数", "type": "str", "required": True},
        {"name": "area", "description": "图像比例(1:2-2:1)", "type": "str", "required": False},
        {"name": "no", "description": "屏蔽词汇", "type": "str", "required": False},
        {"name": "quality", "description": "图像质量(0.25-2.0)", "type": "float", "required": False, "max": 2.0, "min": 0.25},
        {"name": "stylize", "description": "风格化参数(0-1000)", "type": "int", "required": False, "max": 1000, "min": 0},
        {"name": "niji", "description": "动漫化", "type": "int", "required": False, "choice": {"niji 4 (不支持stylize)": 4,"niji 5": 5}},
        {"name": "seed", "description": "图像种子", "type": "int", "required": False, "max":4294967295, "min": 0},
        {"name": "chaos", "description": "图像差异值(0-100)", "type": "int", "required": False, "max":100, "min": 0},
        {"name": "image", "description": "参考图像", "type": "Attachment", "required": False},
        {"name": "imageratio", "description": "参考图像权重(0-15)", "type": "int", "required": False, "max":15, "min": 0},
    ],
    "Version5.1":[
        {"name": "prompt", "description": "图片参数", "type": "str", "required": True},
        {"name": "area", "description": "图像比例(1:2-2:1)", "type": "str", "required": False},
        {"name": "no", "description": "屏蔽词汇", "type": "str", "required": False},
        {"name": "style", "description": "AI联想", "type": "bool", "required": False, "choice": {"打开联想": False,"关闭联想": True}},
        {"name": "quality", "description": "图像质量(0.25-2.0)", "type": "float", "required": False, "max": 2.0, "min": 0.25},
        {"name": "stylize", "description": "风格化参数(0-1000)", "type": "int", "required": False, "max": 1000, "min": 0},
        {"name": "niji", "description": "动漫化", "type": "int", "required": False, "choice": {"niji 4 (不支持stylize)": 4,"niji 5": 5}},
        {"name": "seed", "description": "图像种子", "type": "int", "required": False, "max":4294967295, "min": 0},
        {"name": "chaos", "description": "图像差异值(0-100)", "type": "int", "required": False, "max":100, "min": 0},
        {"name": "image", "description": "参考图像", "type": "Attachment", "required": False},
        {"name": "imageratio", "description": "参考图像权重(0-15)", "type": "int", "required": False, "max":15, "min": 0},
    ],
}

DBlendPromptDic = [
    {"name": "image1", "description": "传入的图片", "type": "Attachment", "required": True},
    {"name": "image2", "description": "传入的图片", "type": "Attachment", "required": True},
    {"name": "dimensions", "description": "图像尺寸", "type": "str", "required": False, "choice": {"2：3 → 半身": "--ar 2:3","1：1 → 矩形": "--ar 1:1","3：2 → 广角": "--ar 3:2"}},
    {"name": "image3", "description": "传入的图片", "type": "Attachment", "required": False},
    {"name": "image4", "description": "传入的图片", "type": "Attachment", "required": False},
    {"name": "image5", "description": "传入的图片", "type": "Attachment", "required": False},
]

DDescribePromptDic = {"name": "image", "description": "传入的图片", "type": "Attachment", "required": True},
