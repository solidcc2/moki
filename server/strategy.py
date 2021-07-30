from abc import ABCMeta
from context import Context

# 策略类
class Strategy(metaclass=ABCMeta):
    def __init__(context):
        self.context = context
    
    @abc.abstractmethod
    def decide():
        pass 

# 策略的实现类
class SimpleStrategy(Strategy):
    def __init__(context):
        super.__init__(context)
        self.speeds = []      # 节点的通信速度估计
        self.deployTime = []  # executor的部署时间估计
        self.executeTime = [] # executor的执行时间估计
    
    def decide():
        # 更新辅助数据，并调用context的工具函数move，deploy，execute执行决策
        
        pass
