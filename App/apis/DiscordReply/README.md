# DiscordReply 文档综述
> 该文档内容主要用于接收Discord的响应

---
## 文档结构
- utils >> StaticClassMethod 存放文件夹
  - __init__.py >> 子文件夹内跨域变量初始文件
  - EmbGene.py >> Embed 类型消息生成
  - MsgGene.py >> Content 类型消息生成，以及消息检测
  - PromptGene.py >> Slash.choice 生成

- exts >> ExtensionsMethod 存放文件夹
  - __init__.py >> 子文件夹内跨域变量初始文件
  - CLMethod.py >> Channel Method 动态方法
  - CPMethod.py >> Component Method 动态方法
  - PPMethod.py >> Prompt Method 动态方法
  
- __init__.py >> 子文件夹内跨域变量初始文件
- BotCommand.py >> 所有的`命令`响应文件
- BotComponent.py >> 所有的`组件`响应文件
- BotEvent.py >> 所有的`监听`响应文件

---
## 注意事项
这个文档中除了`BotEvent`在未来会和数据库有链接,其他的方法仅限于`Discord环境`使用

即此目录下的文件尽可能**不要**与Flask等文件产生牵连,否则影响数据库和队列

Discord Update： 本次更新仅为Discord开辟了两条队列，且为私密队列，与其他队列隔离，在未来会加入队列的定时删除操作

---
## 请求流程
BotCommand -> Slash Command -> Queue.update -> PostAgent <- Queue.update <- BotComponent

BotEvent -> Component Create + Queue.remove

