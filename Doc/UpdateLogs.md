<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/56034408/233843417-32cdc382-88db-4e9e-8d63-272b19d2d5c6.png" alt="DandJourney">
  
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
### Version 2.0 Per-Release
---
- 内容抽离与初始化
- 项目框架重构
- 操作流程优化
- 更新 `/dsettings`命令， `/dblend`、`/describe` 等命令需要进一步测试
- 消息监听优化
- 优化 MidJourney 版本隔离问题
---
---
## **Version 1 Update**
---
- 从[MidJourney-Wrapper](https://github.com/Wildric-Auric/MidJourney-Wrapper)获取分支
- 恢复主体功能
---
### Version 1.1
- 新增机器人的/info 、 /usage 等用法
- 修复机器人Message自触发等bug
---
### Version 1.2
- /dj 指令拓展，支持6种自定义内容
- 指令反馈，完善机器人反馈信息
- 增加用户阻塞，机器人获取相关MessageTarget后会为使用者保留waitTime 秒，默认30s
- 削弱机器人的灵敏度，现在仅在回复MidJourney时会触发机器人
---
### Version 1.3
- 新增/blend 、/fast 、/relax  指令 ( /dblend 方法存在问题 暂时封存 V2.0修复 )
- 更新/dj 垫图功能
- 修复身份串线等恶性bug
- 更新/usage 指令内容
---