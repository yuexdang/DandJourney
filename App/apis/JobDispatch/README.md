# JobDispatch 文档综述
> 该文档内容主要用于处理所有的临时数据结构

---
## 文档结构
- __init__.py >> 子文件夹内跨域变量初始文件
- Dispatcher.py >> 数据结构类

---
## 注意事项
目前仅更新了队列这一种数据结构，同时提供队列管理器用于智能管理所有插入的队列

后续会根据需求添加不同的类型

---
## 请求流程
Outside Request -> JobManager -> (Cls)Queue
