from active import EventType, Event, Active
from enum import Enum
from Queue import Queue

# 命令类型
class CommandType(Enum):
    DEPLOY_MODEL = 0
    EXECUTOR_MODEL = 1
    SET_SAMPLE_CYCLE = 2
    SEND_DATA = 3
    DELETE_DATA = 4
    COPY_DATA = 5

# 命令类
class Command:
    def __init__(self, _type, value=0, ori=0, des=0):
        self.type = _type
        self.value = value
        self.ori = ori
        self.des = des

# worker类，负责接收并解析command
class Worker(Active):
    def __init__(self, mediator, host_id):
        super().__init__(mediator)
        self.host_id = host_id      # 所在主机id
        self.CommandQueueSize = 100 # 命令队列的长度
        self.CommandQueue = Queue(maxsize = self.CommandQueueSize) # 命令队列

    # 接收master的命令并解析
    def run():
        while True:
            if not self.CommandQueue.empty():
                command = self.CommandQueue.get()
                self.CommandQueue.pop()
                if command.type == CommandType.DEPLOY_MODEL:
                    deployEvent = Event(EventType.DEPLOY_MODEL, command.value, 0)
                    self.activate(self, deployEvent)
                elif command.type == CommandType.EXECUTOR_MODEL:
                    executeEvent = Event(EventType.EXECUTE_MODEL, command.value, 0)
                    self.activate(self, executeEvent)
                elif command.type == CommandType.SET_SAMPLE_CYCLE:
                    setCycleEvent = Event(EventType.SET_CYCLE, command.value, 0)
                    self.activate(self, setCycleEvent)
                elif command.type == CommandType.SEND_DATA:
                    sendDataEvent = Event(EventType.SEND_DATA, command.value, [command.ori, command.des])
                    self.activate(self, sendDataEvent)
                elif command.type == CommandType.DELETE_DATA:
                    deleteDataEvent = Event(EventType.DELETE_DATA, command.value, 0)
                    self.activate(self, deleteDataEvent)
                elif command.type == CommandType.COPY_DATA:
                    copyDataEvent = Event(EventType.COPY_DATA, command,value, [command.ori, command.des])
                    self.activate(self, copyDataEvent)
