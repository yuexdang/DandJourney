# 定义队列类, 还没做并发处理

import sys
import datetime

"""
队列与队列管理器Job
用于统一管理项目的队列,分配单时刻的任务
操作Job即可进行队列的插入与删除,以及针对性的查找队列

目前还未完全完成
"""

class QueueCls:
    def __init__(self, queue_name, queue_size, queue_value, is_isolation):
        """
        queue_name : 队列名
        queue_size : 队列大小(非内存大小)
        queue_value : 队列值
        is_isolation : 是否隔离队列(用于智能插入队列模式)
        """
        self.queue_name = queue_name
        self.queue_size = queue_size
        self.queue_value = queue_value
        self.is_isolation = is_isolation
        self.queue = []

    def get_unused_job_id(self, UpJob):
        """
        获取队列未被引用的JobID
        """
        used_ids = [item['JobID'][10:] for item in self.queue]
        _date = datetime.datetime.now().strftime("%m%d%H%M%S")
        if len(used_ids) >= self.queue_size:pass
        else:
            if UpJob:return (True, UpJob)
            for i in range(self.queue_size):
                new_id = "{}{}{}".format(_date, self.queue_name, i)
                if new_id not in used_ids:
                    return (True, new_id)
        return (False, "JobID has already reach limit:{}".format(self.queue_size))

    def insert(self, element, otherKey, UpJob):
        """
        插入队列值
        """
        job_id = self.get_unused_job_id(UpJob)
        if job_id[0]:
            element["JobID"] = job_id[1] + otherKey
            self.queue.append(element)
        return job_id

    def remove(self, job_id):
        """
        删除队列值
        """
        removed_elements = []
        for item in self.queue:
            if item.get('JobID') == job_id:
                self.queue.remove(item)
                removed_elements.append(item)
        return removed_elements

    def find(self, any_key, any_value, dim = None):
        "根据键值对查找队列元素"
        return [item for item in self.queue if item[any_key][:dim] == any_value]

    def extract(self):
        """
        队列验证
        """
        if self.queue:
            return (True, self.queue[0])
        else:
            return (False, "Queue is empty.")

    def last(self, PutAll = False, length = False):
        """
        队列剩余内容输出
        """
        if PutAll:
            return [item for item in self.queue]
        if length:
            return len(self.queue)
        else:
            return [item['JobID'] for item in self.queue]
        
    def get_memory(self):
        """
        获得队列的空间占用
        """
        total_memory = sum(sys.getsizeof(item) for item in self.queue)
        return total_memory


class Job:
    def __init__(self):
        self.queues = {}

    def create_queue(self, queue_name, queue_size, queue_value, is_isolation=False):
        """
        创建队列
        """
        if queue_name not in self.queues:
            self.queues[queue_name] = QueueCls(queue_name, queue_size, queue_value, is_isolation)
            print(f"Queue '{queue_name}' created.")
        else:
            print(f"Queue '{queue_name}' already exists.")

    def delete_queue(self, queue_name):
        """
        删除队列
        """
        if queue_name in self.queues:
            del self.queues[queue_name]
            print(f"Queue '{queue_name}' deleted.")
        else:
            print(f"Queue '{queue_name}' does not exist.")

    def find_queue(self, queue_name):
        """
        根据队列名查找队列
        """
        if queue_name in self.queues:
            return (True, self.queues[queue_name])
        else:
            return (False, f"Queue '{queue_name}' does not exist.")

    def queueList(self):
        """
        输出队列列表
        """
        return [_queue for _queue in self.queues.keys()]
    
    def queueAllItem(self, PutAll = False, length = False):
        """
        输出所有队列的所有元素
        """
        return [self.queues[_queue].last(PutAll, length) for _queue in self.queues.keys()]
    
    def insert_queue(self, queue_name, element, UpJob = "", otherKey = ""):
        """
        向指定队列插入元素
        """
        if queue_name in self.queues:
            queue = self.queues[queue_name]
            inserted_job_id = queue.insert(element, otherKey, UpJob)
            return inserted_job_id, queue_name
        else:
            return (False, "Queue does not exist")

    def insert_queue_S(self, element, authority, NoneQueue, UpJob = "", otherKey = ""):
        """
        智能插入队列模式
        使用此方法插入数据并打开智能插入,会根据条件自动选择满足条件的队列进行插入操作
        目前条件:选择队列长度最短的元素进行插入
        """
        if authority:
            queue_to_insert = min((q for q in self.queues.values() if not q.is_isolation), key=lambda q: q.last(length = True))
        else:
            queue_to_insert = next((q for q in self.queues.values() if q.queue_name == NoneQueue), None)

        if queue_to_insert:
            inserted_job_id = queue_to_insert.insert(element, otherKey, UpJob)
            return inserted_job_id, queue_to_insert.queue_name
        else:
            return (False, "Can't find Queue in JobList")

    def delete_queue_value(self, queue_id, job_id):
        """
        删除指定队列中JobID指向的元素
        """
        if queue_id in self.queues:
            queue = self.queues[queue_id]
            removed_elements = queue.remove(job_id)
            return removed_elements
        else:
            print(f"Queue '{queue_id}' does not exist.")
            return []
        
    def get_memory(self):
        """
        查询队列管理器目前内存
        队列中若出现对象,此算法将失效
        """
        total_memory = sum(queue.get_memory() for queue in self.queues.values())
        return total_memory
