<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/56034408/234861839-7cddd103-e597-4029-b514-063c4bca5227.png" alt="DandJourney">
  
  <h1 align="center">DandJourney Usage</h1>
  <p align="center"> 用爱发电的MidJourney消息转发机器人 </p>
</p>

# 安装方法
<h3 align="center"> <a href="#机器人创建">Discord 机器人</a> | <a href="#机器人部署">DandJourney部署</a> | <a href="#三方平台">三方平台</a> | <a href="#控制台配置">Flask总控</a> </h3>

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
---
## 机器人部署

### 部署前的准备

目前还缺失两个参数：**`BOT_NAME`** 和 **`CHANNEL_SIGN`**
> `BOT_NAME` ☞ 机器人的名称
>
> `CHANNEL_SIGN` ☞ 是否需要适应不同频道(默认为False)

### 快速部署
> 已打包至Railway,初始化的时候把六个参数填入即可
>
>[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/aWVdcq?referralCode=SvAPpE)

#### 本地化部署

> #### 初始化数据
> ---
> 在 [设置文档](https://github.com/yuexdang/DandJourney/blob/main/App/config.py) 中将各个参数填入（没见过的不用管，还在开发）
> 
> 如 BOT_TOKEN = VenvValue.get('BOT_TOKEN') if "BOT_TOKEN" in VenvValue else "_ Add your BOT_TOKEN HERE _ " 中，将" _ Add your BOT_TOKEN HERE _" 替换为你的 BOT_TOKEN 即可（注意：USE_MESSAGED_CHANNEL中填入的是CHANNEL_SIGN的值）
>
> 或者自己初始化一下全局的环境变量，把几个参数添加至环境即可(需要在[__init__.py](https://github.com/yuexdang/DandJourney/blob/main/App/__init__.py)文件的**第一行**前初始化)

> #### 运行代码
> ---
> 1. pip install [requirements.txt](https://github.com/yuexdang/DandJourney/blob/main/requirements.txt)
> 2. run main.py
> 3. 正常的反馈应该是好几个初始化完毕的提示

---

## 三方平台

还没做到这里，做完了再说

---

## 控制台配置

还没做到这里，做完了再说

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