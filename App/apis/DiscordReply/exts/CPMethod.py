# Component Method
from . import interactions, Button, BotSettings

"""
Component Method Group:
这里放置所有的与组件有关的内容
包含组件生成，组件监听，组件删除等功能
"""

# Component Handle
def ActivateButtons(components: list, padding: list) -> tuple:
    """
    Registration：Turns the list of components into an object\\
    components：    组件列表\\
    padding：       组件排布方式
    """
    __tempComList, __tempChecker = [], 0
    if not padding: padding = [5]*5

    if max(padding) > 5: return (False, "The number of components in a single column exceeds the allowed value. Initialization failed")
    
    for __row in padding:
        if __row < len(components[__tempChecker:]):
            __tempComList.append(interactions.ActionRow(*components[__tempChecker : __tempChecker + __row]))
            __tempChecker += __row
        else:
            __tempComList.append(interactions.ActionRow(*components[__tempChecker :]))
            break
    return (True, __tempComList)


# Component Create
def CreateMultipleButtons(ButtonName: list,  styleDic: dict = None, custom_idDic: dict = None, emojiDic: dict = None, padding: list = None, disableDic: dict = None, instantiation: bool = False) -> list or object:
    """
    Component：Generate multiple button\\
    ButtonName：    按钮组件名称列表\\
    custom_id：     按钮识别码,无规定则与ButtonName一致 Usage : {ButtonName : ButtonID}\\
    style:          按钮样式 Usage : {ButtonName : ButtonStyle} \\
    emoji：         是否使用表情符号 Usage : {ButtonName : ButtonEmoji}\\
    disable：       需要禁用的按钮列表 Usage : {ButtonName : Disabled}\\
    
    padding：       组件排布方式\\
    instantiation： 是设置是否需要实例化按钮列表
    """
    __components = []
    if len(ButtonName) >= 25: return (False, "Description The number of messages reached the upper limit. Initialization failed")

    for _name in ButtonName:
        __components = CreateSingleButton(
                                                ButtonName = _name, 
                                                style = 2 if styleDic is None or _name not in styleDic else styleDic[_name],
                                                custom_id = _name if custom_idDic is None or _name not in custom_idDic else custom_idDic[_name],
                                                emoji = None if emojiDic is None or _name not in emojiDic else emojiDic[_name],
                                                disable = None if disableDic is None or _name not in disableDic else disableDic[_name],
                                                components = __components
                                            )
    return ActivateButtons(__components, padding) if instantiation else (True, __components)

def CreateSingleButton(ButtonName: str, style: int = 2, custom_id: str = None, emoji: str = None, disable: bool = False, components: list = [], index: int = None, instantiation: bool = False) -> list:
    """
    Component：Generate single button\\
    ButtonName:    按钮名称\\
    style:         按钮样式\\
    custom_id：    按钮识别码,无规定则与ButtonName一致\\
    emoji：        是否使用表情符号\\
    disable：      是否禁用按钮\\
    
    components：   需要添加新按钮的列表\\
    index：        新按钮插入的位置\\
    instantiation：是否需要实例化按钮列表
    """
    components.insert(len(components) if index is None else index, Button(style = style, custom_id = custom_id if custom_id else ButtonName, label = ButtonName, emoji = emoji, disabled = disable))
    return ActivateButtons(components) if instantiation else components

# Component Delete


# Component Check
def ButtonClick(ctx: interactions.ComponentContext, styleNeed: int = 1, disable: bool = True, Switch: list = []) -> list:
    """
    Component：Click Button Method\\
    ctx 是按钮事件的CommandContext
    styleNeed 是指定按钮样式，默认为启用状态
    disable 是指定按钮可用性，默认禁用
    Switch 是切换列表，默认为更改按钮模式
    """
    __tempList = []
    __buttonList = [interactions.ButtonStyle.PRIMARY, interactions.ButtonStyle.SECONDARY, interactions.ButtonStyle.SUCCESS, interactions.ButtonStyle.DANGER]
    for __action in ctx.message.components:
        __SecList = []
        for __component in __action.components:
            button = Button(style = __component.style, custom_id = __component.custom_id, label = __component.label, disabled = __component.disabled)
            if Switch:
                # 按钮状态切换
                if __component.custom_id == BotSettings[Switch[0]][Switch[1]] or __component.custom_id == ctx.component.custom_id:
                    button.style = __buttonList[1] if str(__component.style)=="1" else __buttonList[0] 
                    button.disabled = False if __component.disabled else True
            else:
                # 按钮状态设置
                if __component.custom_id == ctx.component.custom_id:
                    button.style = __buttonList[styleNeed-1]
                    button.disabled = disable
                else: pass
            __SecList.append(button)
        __tempList.append(__SecList)
    return __tempList