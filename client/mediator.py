from active import EventType
from data import DataPool, DataSample
from executor import Executor
from master import Master, MessageType, Message
from worker import Worker

class Mediator: # 每个host一个实例，负责master,worker,executor,data_sampler之间的沟通
    def __init__(host_id):
        self.host_id = host_id
        self.DATA_POOL = DataPool(host_id)         # 初始化数据池
        self.GPUs = 8                              # 单节点GPU数量
        self.DATA_SAMPLE_CAPACITY = 256            # 采集信息的容量
        self.DATA_SAMPLE = []                      # 节点的数据采样集合
        self.executors = []                        # 节点的执行器集合
        for i in range(GPUs):                      # 开辟GPU数量个数据采样和执行进程         
            self.DATA_SAMPLE.append(DataSample(self, host_id, i, 10)) # 新建初始化数据采样池并加入集合
            self.executors.append(Executor(self, host_id, i))         # 新建执行器并加入集合
        self.worker = Worker(mediator, host_id)    # 节点的worker,负责接收server下达的命令并解析
        self.master = Master(mediator, host_id)    # 节点的master,负责向server发送数据
        
    def changed(entity, event):
        # 判断event类型
        if event.type == EventType.SUBMIT_DATA:
            # 接收数据成功
            receivedDataMsg = Message(MessageType.RECEIVED_DATA, [entity.host_id, entity.id], event.key)
            self.master.report(receivedDataMsg)
        elif event.type == EventType.DEPLOYE_MODEL_COMPLETE:
            # 向master上报模型部署完成
            deploydModelCompleteMsg = Message(MessageType.DEPLOY_MODEL_COMPLETE, [entity.host_id, entity.id], event.key)
            self.master.report(deploydModelCompleteMsg)
        elif event.type == EventType.EXECUTE_COMPLETE:
            # 向master上报executor执行完成
            executorModelCompleteMsg = Message(MessageType.EXECUTE_MODEL_COMPLETE, [entity.host_id, entity.id], event.key)
            self.master.report(executorModelCompleteMsg)
        elif event.type == EventType.SAMPLE_GEN:
            # 将采集到的数据置于队列中并完成上报
            if len(self.DATA_SAMPLE) < self.DATA_SAMPLE_CAPACITY:
                self.DATA_SAMPLE.append(event.value)
            else:
                dataSubmitMsg = Message(MessageType().SAMPLE_GEN, self.host_id, self.DATA_SAMPLE)
                self.master.report(dataSubmitMsg)
                # 清空DATA_SAMPLE
                self.DATA_SAMPLE = []
        elif event.type == EventType.DEPLOY_MODEL:
            # 部署模型, event.key: [第几个executor, 需要部署的model_name]
            self.executors[event.key[0]].deploye_model(event.key[1])
        elif event.type == EventType.EXECUTE_MODEL:
            # 执行模型, event.key: [第几个executor, 需要执行的model_name, 输入数据的id]
            input_data = self.DATA_POOL.get(event.key[2])
            self.executors[event.key[0]].run_model(event.key[1], input_data)
        elif event.type == EventType.SET_CYCLE:
            # 设置采样周期 event.key: cycle
            for i in range(self.GPUs):
                self.DATA_SAMPLE[i].setCycle(event.key)
        elif event.type == EventType.SEND_DATA:
            # 发送数据 event.key: data id event.value: ori host id, des host id
            # 获取数据
            data = self.DATA_POOL.get(event.key)
            # 从本机删除数据
            self.DATA_POOL.delete(event.key)
            # 发送数据到目的主机
            
        elif event.type == EventType.DELETE_DATA:
            # 删除数据 event.key: data id 
            self.DATA_POOL.delete(event.key)
        elif event.type == EventType.COPY_DATA:
            # 获取数据
            data = self.DATA_POOL.get(event.key)
            # 发送数据到目标主机

            
        