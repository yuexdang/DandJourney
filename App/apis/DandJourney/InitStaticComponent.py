from .BotComponent import UVEditorGenerate, VersionGenerate
from .utils.component import CreateMultipleButtons, CreateSingleButton

from . import agentBot



UVBotton = ["U1", "U2", "U3", "U4", "V1", "V2", "V3", "V4", "🔁 Refresh", "🈴 Mix Them"]

# 初始化 UVEditor
UVComponent = CreateMultipleButtons(ButtonName = UVBotton, custom_idDic = {"🔁 Refresh":"Refresh", "🈴 Mix Them":"BlendG"}, padding = [4,4,2], instantiation = True)
UVComponent = UVComponent[1] if UVComponent[0] else None
UVEditorGenerate(UVBotton[:-2])
print("UV按钮初始化完毕")


SettingButton = ["Fast", "Relax", "V1", "V2", "V3", "V4", "V5"]

# 初始化 Setting
# 这里不能把按钮也同步初始化了，不然后面调用dsetting会不更新状态
VersionGenerate(["Version"+_button[-1] for _button in SettingButton[-5:]])
print("Setting按钮初始化完毕")

MakeVButton = ["🔉 Describe", "🎁 Make Variations"]

# 初始化 MakeVComponent
MakeVComponent = CreateMultipleButtons(ButtonName = MakeVButton, custom_idDic = {"🔉 Describe": "DescribeU", "🎁 Make Variations": "VariationU"}, padding = [2], instantiation = True)
MakeVComponent = MakeVComponent[1] if MakeVComponent[0] else None
print("MakeVComponent按钮初始化完毕")
