import random
import datatime
import schedule
from active import EventType, Event, Active

# 数据池
class DataPool:
    def __init__(host_id):
        self.DATA_POOL = {}    # 数据池
        self.host_id = host_id # 数据池放置的host id
    
    def get(_id):
        if _id not in DATA_POOL.keys():
            print(str(_id) + " is not in data pool keys.")
            return -1
        else:
            return self.DATA_POOL[_id]
    
    def set(key, value):
        self.DATA_POOL[key] = value

    def delete(key):
        if key in self.DATA_POOL.keys:
            self.DATA_POOL.pop(key)

# 数据采样池
class DataSample(Active):
    def __init__(mediator, host_id, id, cycle):
        super().__init__(mediator)
        self.DATA_SAMPLE = {}  # 数据采样池
        self.host_id = host_id # 数据采样池放置的host id
        self.id = id           # 数据采样池的id
        self.cycle = cycle     # 采样周期
        self.seed = datatime.datatime.now() # 设置采样种子
    
    def get():
        return 
        random.seed(self.seed)
        return random.random()

    def setCycle(cycle):
        self.cycle = cycle

    def run(): # 按照cycle，进行数据上报
        # 循环进行数据采集并进行上报
        num = 0
        while True:
            DataGenEvent = Event(EventType.SAMPLE_GEN, num, self.get())
            num += 1
            self.activate(self, DataGenEvent)
            time.sleep(self.cycle)
