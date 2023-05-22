<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/56034408/234861839-7cddd103-e597-4029-b514-063c4bca5227.png" alt="DandJourney">
  
  <h1 align="center">DandJourney Usage</h1>
  <p align="center"> 用爱发电的MidJourney消息转发机器人 </p>
</p>

# 安装方法
<h3 align="center"> <a href="#机器人创建">Discord 机器人</a> | <a href="#机器人部署">DandJourney部署</a> | <a href="#三方平台">三方平台</a> | <a href="#控制台配置">Flask总控</a> | <a href="#配置参数表">配置参数表</a> </h3>

---
## 机器人创建

这里需要获得[机器人的`token`](#注册一个机器人)、[订阅用户的`authorization`](#氪金玩家的代号)、[Discord系列`ID`](#获得频道信息)，如果有相关的机器人开发经验，或者是已经明白如何获得相关参数，可以[跳过这里](#机器人部署)

### **注册一个机器人**

> **进入[Discord开发者平台](https://discord.com/developers/applications)**
>
> 点击注册组件
> ![image](https://user-images.githubusercontent.com/56034408/234901003-c8090666-871c-4fc3-abb6-84f39b372bdb.png)

> **点击注册组件并填写信息**
> 
> ![image](https://user-images.githubusercontent.com/56034408/234901557-2241bca0-2e13-4055-9e76-7c609620c69a.png)

> **点击Bot进入机器人设置页面**
>
> ![image](https://user-images.githubusercontent.com/56034408/234902683-50689294-0284-4f50-a6f1-b2ba778e9245.png)

> **勾选下方的三个选项(是否允许机器人收发消息等)并获得变量 `BOT_TOKEN(String)`**
>
> ![image](https://user-images.githubusercontent.com/56034408/234903012-1613a505-ddb0-47ff-a008-65cf38b339ff.png)
> ![image](https://user-images.githubusercontent.com/56034408/234903351-1cfeed6a-0fd4-44c9-b0bf-591d041f97a6.png)

> **点击OAuth2 -> URL Generator，调整设置生成链接**
> 
> ![image](https://user-images.githubusercontent.com/56034408/234903554-10d48c0c-899d-4e67-adbe-540b51a756b8.png)
> ![image](https://user-images.githubusercontent.com/56034408/234918620-01c989a3-0a5f-4bb0-89f4-4f3c18cc9f25.png)

> **访问生成的链接，选择服务器，任务完成🎉**

### **获得频道信息**

> **进入你所需要的频道**
>
> 此时url的内容为 **https://discord.com/channels/ `SERVER_ID(Integer)` / `CHANNEL_ID(Integer)`**

### **氪金玩家的代号**

> **使用氪金账号随便执行一条指令**
>
> 在开发者工具 -> 网络 中找到最近的 **interactions** 请求，在请求标头中找到 **authorization: `VIP_TOKEN(String)`** 

### 自此，关于DandJourney宏观配置的**四个变量**已经收集完毕

> Tips: 需要将机器人的配置设置为如图所示，以免自带参数影响图片生成
> ![image](https://github-production-user-asset-6210df.s3.amazonaws.com/56034408/239992841-5fa33f9a-a278-4284-894b-7e173290376f.png)
---
## 机器人部署

### 部署前的准备

目前还缺失两个参数：**`BOT_NAME`** 和 **`CHANNEL_SIGN`**
> `BOT_NAME` ☞ 机器人的名称
>
> `CHANNEL_SIGN` ☞ 是否需要适应不同频道(默认为True)

### 快速部署
> 已打包至Railway,初始化的时候把参数填入即可
>
>[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/aWVdcq?referralCode=SvAPpE)

#### 本地化部署

> #### 初始化数据
> ---
> 在 [mainOffline.py](../mainOffline.py) 中填入所需参数

> #### 运行代码
> ---
> **Python 3.11+**
> 1. pip install [requirements.txt](../requirements.txt) 
> 2. run mainOffline.py
> 3. 正常的反馈应该是好几个初始化完毕的提示

---

## 三方平台

还没做到这里，做完了再说

---

## 控制台配置

还没做到这里，做完了再说

---

## 配置参数表

DandJourney涉及的所有可配置参数如下表所示

| 参数 | 配置 | 说明(没有/不需要则忽视) | 是否必须 |
| ---- | ---- | ---- | ---- |
|BOT_TOKEN|String|搭载机器人的令牌|True|
|SERVER_ID|String|服务器ID|True|
|VIP_TOKEN|String|拥有权限的账号Token|True|
|CHANNEL_ID|String|初始频道|True|
|BOT_NAME|String|机器人名字|True|
|CHANNEL_SIGN|True|是否需要MJ跟随用户|True|
|AGENT_CHANNEL|String|MJ消息汇总频道|False|
|PROXY_URL|String|代理服务器链接|False|
|PROXY_AUTH|Tuple|代理服务器账号密码|False|
|MID_JOURNEY_ID|String|MJ机器人ID|False|

---

# 命令集
```
    /dj (图片参数) (图片尺寸) (图片质量) (风格化) (图片种子) (图组差异化) (参考图片) (参考图片权重) -- 生成图片 [各版本要求不一致]
    /dblend (图片) (图片) (图片) (图片) (图片) (图片差异化) -- 融合图片
    /describe (图片) -- 描述图片
    /dsettings -- 调整DandJourney相关参数
    /dabout -- 关于DandJourney
    /dhelp -- DandJourney使用帮助
```

---

# 一些示例

简单介绍一下一些交互效果

> **/dj `prompt` `area` `quality` `stylize` `seed` `chaos` `image` `imageratio`** 等需要输入参数的命令
>
> ![image](https://user-images.githubusercontent.com/56034408/234924096-79c5c480-6305-4fdc-9776-c7c0caab0729.png)

> **/dabout** 等不需要输入参数的命令
>
> ![image](https://user-images.githubusercontent.com/56034408/234921641-259be110-29ca-4c99-a73e-40cdb07eda5e.png)

> 消息接收后的细化反馈太长了截图不好看，欢迎尽情体验

---

### 感谢使用~