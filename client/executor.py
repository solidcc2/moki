from enum import Enum
from active import EventType, Event, Active
import torch

class ExecutorState(Enum):
    # Executor的状态
    IDLE = 0
    DEPLOYED = 1
    RUNNING = 2
    TERMINATION = 3

class Executor(Active):
    def __init__(self, mediator, host_id, _id):
        super().__init__(mediator)
        self.state = ExecutorState.IDLE
        self.host_id = host_id           # 所在主机id
        self.id = _id                    # executor id
        self.models = []                 # 当前exector的model列表
        self.device = torch.device("cuda:" + str(id) if torch.cuda.is_available() else "cpu") # 设置device
        self.results = []                # 保存执行结果 {{model1：[{0: res0}, {1: res1}]},{model2: [{0: res0}, {1: res1}]}}

    # 重写进程类的run方法
    def run():
        # 轮询接受命令，执行相应动作
        print("host" + str(self.host_id) + " executor " + str(self.id) + " start. ")
        # 循环判断是否从其他worker接收到数据
        while True:
            # 接收成功则触发submitEvent
            pass

    # 改变executor状态
    def setState(state):
        self.state = state

    # 提交数据
    def submitData(key, value):
        # 封装Event事件，向mediator发送提交数据请求，让mediator将数据文件写入Data pool
        submitEvent = Event(EventType.SUBMIT_DATA, key, value)
        self.activate(self, submitEvent)

    # 部署模型
    def deploye_model(model_name):
        # 查找到model
        model = load_model(model_name)
        # 将模型放入内存，将模型执行结构与显存的映射关系建立
        models.append(model)
        # 加入pipeswitch中相关的显存映射逻辑

        # 通知master节点模型部署完成
        deployedEvent = Event(EventType.DEPLOYE_MODEL_COMPLETE, model_name, 0)
        self.activate(self, deployedEvent)
        # 修改executor状态
        self.state = ExecutorState.DEPLOYED

    # 执行模型
    def run_model(model_name, input_data):
        # 在models里面查找到模型
        model = find(model_name)
        # 改变executor状态到running
        self.state = ExecutorState.RUNNING
        # 开始执行
        output_data = model.forward(input_data.to(self.device))
        # 将输出结果加入数据池
        self.report[model_name].append(output_data)
        # 通知master模型执行完成
        executedEvent = Event(EventType.EXECUTE_COMPLETE, model_name, 0)
        self.activate(self, executedEvent)
        # 将状态变为idle
        self.state = ExecutorState.IDLE

    # 获取executor状态
    def getState():
        return self.state
    
    # 获取运行结果，第几个模型的第几次执行结果
    def getResult(model_name, id):
        if model_name not in self.results.keys:
            print(model_name + " have not be executored.")
            return -1
        data = self.results[model_name]
        if id >= len(data):
            print(model_name + " be executored " + len(data) + " times, but you query the " + id + " times.")
            return -2
        return data[id]

    # 清空运行结果
    def clearResult(model_name="all", index="all"):
        if model_name == "all": # 清空所有缓存结果
            self.results.clear()
        elif model_name not in self.results.keys:
            return
        elif index == "all":    # 清空相应模型所有缓存结果
            self.results[model_name] = []
        elif index >= len(self.results[model_name]):
            return
        else:
            self.results[model_name].pop(index)




        




        
