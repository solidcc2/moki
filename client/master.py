from active import EventType, Event, Active
from enum import Enum

# 消息类型
class MessageType(Enum):
    RECEIVED_DATA = 0
    DEPLOY_MODEL_COMPLETE = 1
    EXECUTE_MODEL_COMPLETE = 2
    SAMPLE_GEN = 3

# 消息类
class Message:
    def __init__(self, _type, origin=0, value=0):
        self.type = _type
        self.origin = origin
        self.value = value

# master类，负责向server汇报消息
class Master(Active):
    def __init__(self, mediator, host_id):
        super().__init__(mediator)
        self.host_id = host_id # 所在主机id
        # grpc 通信子

    # 负责接收worker传过来的信息并做出决策
    def run():
        while True:
            pass

    # 向controller上报数据
    def report(msg):
        # 传递message到server
        pass