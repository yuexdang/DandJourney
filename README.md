<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/56034408/234861839-7cddd103-e597-4029-b514-063c4bca5227.png" alt="DandJourney">

  <h1 align="center">DandJourney</h1>
  <p align="center"> 用爱发电的MidJourney消息转发机器人 </p>
</p>

<p align="center">
  <a href="#">
    <img alt="语言类型" src="https://img.shields.io/badge/language-Python-blue?style=flat&logo=python&logoColor=white" />
  </a>
  <a href="./Docs/UpdateLogs.md">
    <img alt="更新日志" src="https://img.shields.io/badge/Update--Log-ClickHere-brightgreen?style=flat&logo=uploaded&logoColor=white" />
  </a>
  <a href="#">
    <img alt="支持平台" src="https://img.shields.io/badge/chat-discord-blue?style=flat&logo=discord&logoColor=white" />
  </a>
   <a href="#">
    <img alt="支持平台" src="https://img.shields.io/badge/chat-wechat-green?style=flat&logo=wechat&logoColor=white" />
  </a>
</p>

<p align="center">
  <a href="#">
    <img alt="zh-cn" src="https://img.shields.io/badge/-%E4%B8%AD%E6%96%87-blue" />
  </a> 
  <a href="./README_EN.md">
    <img alt="en" src="https://img.shields.io/badge/-ENGLISH-lightgrey" />
  </a> 
</p>

# 关于DandJourney

DandJourney 是一款封装与拓展了 Midjourney 的代理机器人。这个机器人主要用来转发用户诉求给MidJourney（位于Discord平台），通过机器人的代理，平衡了用户的机器人使用需求，同时尝试在不同的平台上进行机器人拓展。

- 更多的平台支持（开发中）
- 更多的自定义功能
- 更多的拓展空间

### 为什么不用stable-diffusion

stable-diffusion虽然免费，但是基于神经网络的训练十分消耗自己和电脑的寿命，性能与数据库影响了整体的出图质量与效率。在没有更好的算法产生之前，先暂时用着MidJourney也不失为一个好的选择。

### 项目进程

在没有更好的载体的情况之下，这个项目会持续更新。

项目是**开源**的，Bot的制作只是为了方便平时的使用。禁止非项目组成员使用项目去**盈利**或**引流**。

声明：此机器人仅用于学习使用

# 功能列表
|  功能  | 简介 | 状态 |
|  ----  | ----  | ---- |
| 基础功能 | 支持/imagine、/fast、/relax、图片细分等功能 | ✅ |
| 用户隔离 | 用户消息隔离 | ✅ |
| discord支持  | 支持在discord平台使用此功能 | ✅ |
| 微信支持  | 支持微信聊天 | 🚧 |
| QQ 支持  | 支持QQ聊天 | 🚧 |
| 斜杠指令  | 支持Discord 斜杠指令 | ✅ |
| 更多的功能拓展 | 在原始MidJourney功能基础上拓展更多的指令 | ✅ |
| 风格化预设 | 支持多种风格化图片生成 | 🚧 |
| 更好的交互 | 改版用户界面 | 🚧 |
| Flask App | Flask支持 | 🚧 |

# 项目迭代

可能你是从 [MidJourney-Wrapper（Yuexdang重构版）](https://github.com/yuexdang/MidJourney-Wrapper) 这里来的。我想再次说明一下这两个项目的关系。

这次的重构和之前原作者的代码已经大不一样了，使用的是`discord-py-interactions`框架进行的搭建，爬虫部分也进行了修改，整体代码进行了降耦合，并打算在后面进行API抽离。所以我不打算再称之为重构版本或者是继承版本，而是从头开始做起的一个新项目。

在此再次感谢原作者[Wildric-Auric](https://github.com/Wildric-Auric)与我最早接触到的版本[MidJourney-Wrapper](https://github.com/Wildric-Auric/MidJourney-Wrapper)，最原始的思路对我的帮助很大。

# 使用用法

> ### **快速部署**
>
>[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/aWVdcq?referralCode=SvAPpE)

> ### **本地部署**
>
>具体的使用方法详见[使用文档](./Docs/Usage.md).

# 更新日志

更新日志详见[更新日志](./Docs/UpdateLogs.md)。

# 志同道合的朋友们（贡献者）


<table>
<thead>
  <tr>
    <th colspan="3">贡献成员列表（各部分贡献自高向低排序）</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>分类</td>
    <th>成员</td>
    <th>贡献说明</td>
  </tr>
  <tr>
    <td>框架构建</td>
    <td><a href="https://github.com/yuexdang">yuexdang</a></td>
    <td>整体代码功能实现、需求实现</td>
  </tr>
  <tr>
    <td rowspan="3">功能代码研究</td>
    <td><a href="https://github.com/DronerC">DronerC</a></td>
    <td>代码抽离、功能发散</td>
  </tr>
  <tr>
    <td><a href="https://github.com/JerryLiu666">JerryLiu666</a></td>
    <td>代码抽离、功能发散</td>
  </tr>
  <tr>
    <td><a href="https://github.com/siyuekoo">siyuekoo</a></td>
    <td>前端代码</td>
  </tr>
  <tr>
    <td rowspan="5">图片风格化研究</td>
    <td><a href="https://github.com/Lin600">Lin600</a></td>
    <td>图像风格化</td>
  </tr>
  <tr>
    <td><a href="https://github.com/mercuryxlloo">mercuryxlloo</a></td>
    <td>图像风格化</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SCkang21">SCkang21</a></td>
    <td>图像风格化</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SimonYu13">SimonYu13</a></td>
    <td>图像风格化</td>
  </tr>
  <tr>
    <td><a href="https://github.com/unbengab19">unbengab19</a></td>
    <td>图像风格化</td>
  </tr>
  <tr>
    <td>文档编纂与维护</td>
    <td><a href="https://github.com/Zhaoci0204">Zhaoci0204</a></td>
    <td>文档编写</td>
  </tr>
  <tr>
    <td>Special UI</td>
    <td><a href="https://github.com/ppapatrick">ppapatrick</a></td>
    <td>图像制作，Icon制作</td>
  </tr>
  <tr>
    <td rowspan="2">其他贡献者</td>
    <td><a href="https://github.com/liustar1989">liustar1989</a></td>
    <td>提供部分wechat连接思路</td>
  </tr>
  <tr>
    <td><a href="https://github.com/xxvcxxvc">xxvcxxvc</a></td>
    <td>图片转存逻辑与其他代码</td>
  </tr>
  <tr>
    <th></th>
    <th></th>
    <th></th>
  </tr>
</tbody>
</table>



### 我也想变成贡献者

符合以下几个条件其一的朋友可以加入贡献者团队中
- 发现了很严重的bug，且给出了有效的修复方法
- 提供了新的功能，并且给出了相关的代码
- 给出了3个及以上的功能需求（评估有效且能够实现）

# 如果想要使用这个源码

如果我们的这个项目可以帮助大家更好的去使用Midjourney，并且使用的非常愉快，请帮忙点一个 **Star** ，这样我们项目组会更有动力去更新与迭代，感谢各位。
