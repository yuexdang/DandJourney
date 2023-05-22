<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/56034408/234861839-7cddd103-e597-4029-b514-063c4bca5227.png" alt="DandJourney">
  
  <h1 align="center">DandJourney UpdateLog</h1>
  <p align="center"> 用爱发电的MidJourney消息转发机器人 </p>
</p>

# 更新日志



---
## **Version 2 Update**
---
- 继承 [MidJourney-Wrapper(Yuexdang重构版)](https://github.com/yuexdang/MidJourney-Wrapper)所有内容
- 完全重构项目代码，对象抽离，操作流程优化
- 命令库更新，命令范围更新
- 增加组件体系，功能优化
---
### Version 2.0.1
---
> For Discord Update **Released**
- DiscordReply(原DandJourney文件)内容重构
- 项目整体代码重构升级
- Discord界面再次优化
- 更新  `/dblend`、`/describe` 等命令以及一系列按钮
- 更新MidJourney V 5.1参数,更新全版本参数
- 消息监听逻辑重构,用户信息抽离,机器人频道隔离
- 优化参数输入问题
- 支持Proxy代理,提供线下环境运行文件`mainOffline.py`
> Bugs: Discord渲染问题,现在通过slash command生成的embed中包含的图像无法正常渲染(DDescribe功能无法将信息绑定至用户, U.Describe失效) [已修复dabout指令]
>
> Bugs: 队列十分依赖生成时序(每一条message都没有能够一直跟踪下来的内容),正常情况可以正常使用,若出现网络波动等情况可能造成用户混乱
---
### Version 2.0 Pre-Release
---
- 内容抽离与初始化
- 项目框架重构
- 操作流程优化
- 更新 `/dsettings`命令， `/dblend`、`/describe` 等命令需要进一步测试
- 消息监听优化,移除用户阻塞
- 优化 MidJourney 版本隔离问题
---
---
## **Version 1 Update**
---
- 从[MidJourney-Wrapper](https://github.com/Wildric-Auric/MidJourney-Wrapper)获取分支
- 恢复主体功能
---
### Version 1.3
- 新增/blend 、/fast 、/relax  指令 ( /dblend 方法存在问题 暂时封存 V2.0修复 )
- 更新/dj 垫图功能
- 修复身份串线等恶性bug
- 更新/usage 指令内容
---
### Version 1.2
- /dj 指令拓展，支持6种自定义内容
- 指令反馈，完善机器人反馈信息
- 增加用户阻塞，机器人获取相关MessageTarget后会为使用者保留waitTime 秒，默认30s
- 削弱机器人的灵敏度，现在仅在回复MidJourney时会触发机器人
---
### Version 1.1
- 新增机器人的/info 、 /usage 等用法
- 修复机器人Message自触发等bug
---