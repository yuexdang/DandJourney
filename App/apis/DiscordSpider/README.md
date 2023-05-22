# DiscordSpider 文档综述
> 该文档内容主要用于向Discord发送请求
>
>若需要接收请求，请查阅 DiscordReply.README 文档

---
## 文档结构
- utils >> StaticClassMethod 存放文件夹
  - __init__.py >> 子文件夹内跨域变量初始文件
  - Globals.py >> 所有请求的配置文件，包含每个请求的SessionID、ID、Version
  - payload.py >> 所有请求的内容文件
- __init__.py >> 子文件夹内跨域变量初始文件
- Spider.py >> 爬虫请求文件

---
## 请求流程
ClassicObject -> (Class)Spider -> payload + Globals -> GetResponse() -> return (Boolean, Response)
