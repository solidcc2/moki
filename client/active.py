from multiprocessing import Process
from mediator import Mediator
from enum import Enum

# 事件的类型
class EventType(Enum):
    # 向master汇报的event
    SUBMIT_DATA = 0             # 提交数据事件，修改DATA_POOL
    DEPLOYE_MODEL_COMPLETE = 1  # 模型部署完成，通知master
    EXECUTE_COMPLETE = 2        # executor执行完成，通知master
    SAMPLE_GEN = 3              # 生成采样数据，修改DATA_SAMPLE
    # 由worker下达的event
    DEPLOY_MODEL = 4            # 部署模型
    EXECUTE_MODEL = 5           # 执行模型
    SET_CYCLE = 6               # 设置采样周期
    SEND_DATA = 7               # 发送数据
    DELETE_DATA = 8             # 删除数据
    COPY_DATA = 9               # 拷贝数据

# 事件类，包括事件类型和数据
class Event:
    def __init__(self, _type, key, value):
        self.type = _type
        self.key = key
        self.value = value

class Active(Process):
    # 构造方法
    def __init__(self, mediator):
        # 使用super函数调用父类的构造方法，并传入相应的参数值。
        super().__init__(self)
        self.mediator = mediator
    
    # activate函数 调用mediator的change方法
    def activate(self, entity, event): # 是谁上报，上报的什么东西
        self.mediator.changed(entity, event)
