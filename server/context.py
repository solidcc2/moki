from reporter import Reporter
from strategy import SimpleStrategy
from controller import Controller
from client.master import MessageType, Message

# 节点类
class Node:
    def __init__(uuid):
        self.uuid = uuid

# 内容类
class Context:
    def __init__():
        self.nodeNum = 4 # 节点数量
        self.nodes = []  # 节点信息
        self.reporter = Reporter(self)       # reporter
        self.strategy = SimpleStrategy(self) # strategy
        self.controller = Controller(self)   # controller
    
    # 更新context信息并触发决策
    def update(message):
        # 某个主机收到了数据
        if message.type == MessageType.RECEIVED_DATA:
            pass
        # 某台主机上的某个executor部署完了模型
        elif message.type == MessageType.DEPLOY_MODEL_COMPLETE:
            pass
        # 某台主机上的某个executor执行完了模型
        elif message.type == MessageType.EXECUTE_MODEL_COMPLETE:
            pass
        # 某台主机上报采集到的状态信息
        elif message.type == MessageType.SAMPLE_GEN:
            pass
        # 进行决策
        self.strategy.decide()
        
        # 从一个主机向另一个主机移动数据
    def move(data_key, src, dst):
        self.controller.move(data_key, src, dst)

    # 从一个主机向另一个主机拷贝数据
    def copy(data_key, src, dst):
        self.controller.copy(data_key, src, dst)

    # 部署模型
    def deploy(host_id, executor_id, model_name):
        self.controller.deploy(host_id, executor_id, model_name)

    # 执行模型
    def execute(host_id, executor_id, model_name):
        self.controoler,execute(host_id, executor_id, model_name)