from context import Context
from multiprocessing import Process
from Queue import Queue

class Reporter(Process):
    def __init__(context):
        self.context = context
        self.MessageQueueSize = 256 # 消息队列的长度
        self.messages = Queue(maxsize = self.MessageQueueSize) # server收到的消息队列
        # grpc的通信子
    
    # 运行体,轮询处理信息队列
    def run():
        while True:
            if not self.messages.empty():
                msg = self.messages.get()
                self.messages.pop()
                self.report(msg)

    # 获取client提交的message
    def getMsg():
        pass

    # 提交给context处理信息
    def report(message):
        self.context.update(message)