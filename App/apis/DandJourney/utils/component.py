from . import interactions, Button, agentBot


"""
方法禁用了，纯纯的蠢蛋行为去造轮子，不会再干这种没有任何意义，还浪费时间和空间的事情了

受不了复制粘贴代码，还是造轮子吧，对不起做不到
"""


def ActionButton(components: list, padding: list) -> object:
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
            __tempComList.append(interactions.ActionRow(components = components[__tempChecker : __tempChecker + __row]))
            __tempChecker += __row
        else:
            __tempComList.append(interactions.ActionRow(components = components[__tempChecker :]))
            break

    return (True, __tempComList)


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

    return ActionButton(__components, padding) if instantiation else (True, __components)


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
    return ActionButton(components) if instantiation else components

    
def ButtonClick(ctx: interactions.CommandContext, styleNeed: int = 1, disable: bool = True, Switch: list = []) -> list:
    """
    按钮处理工作\\
    ctx 是按钮事件的CommandContext
    styleNeed 是指定按钮样式，默认为启用状态
    disable 是指定按钮可用性，默认禁用
    Switch 是切换列表，默认为更改按钮模式
    """
    __tempList = []
    for __action in ctx.message.components:
        __SecList = []
        for __component in __action.components:
            button = Button(style = __component.style, custom_id = __component.custom_id, label = __component.label, disabled = __component.disabled)
            if Switch:
                # 按钮状态切换
                if __component.custom_id == agentBot[Switch[0]][Switch[1]] or __component.custom_id == ctx.component.custom_id:
                    button.style = 2 if "PRIMARY" in str(__component.style) else 1
                    button.disabled = False if __component.disabled else True
            else:
                # 按钮状态设置
                if __component.custom_id == ctx.component.custom_id:
                    button.style = styleNeed
                    button.disabled = disable
                else: pass
            __SecList.append(button)
        __tempList.append(interactions.ActionRow(components=__SecList))
    return __tempList