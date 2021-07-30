from client.worker import CommandType, Command

# Controller类，给client下达command
class Controller:
    def __init__():
        # grpc 通信子
        pass

    # 从一个主机向另一个主机移动数据
    def move(data_key, src, dst):
        # 构造command
        moveCommand = Command(CommandType.SEND_DATA, data_key, src, dst)
        # 通过grpc发送command

    # 从一个主机向另一个主机拷贝数据
    def copy(data_key, src, dst):
        # 构造command
        copyCommand = Command(CommandType.COPY_DATA, data_key, src, dst)
        # 通过grpc发送command

    # 部署模型
    def deploy(host_id, executor_id, model_name):
        # 构造command
        deployCommand = Command(CommandType.DEPLOY_MODEL, [executor_id, model_name])
        # 使用grpc向相应host_id的主机发送command

    # 执行模型
    def execute(host_id, executor_id, model_name):
        # 构造command
        executeCommand = Command(CommandType.EXECUTE_MODEL, [executor_id, model_name])
        # 使用grpc向相应的host_id的主机发送command
        