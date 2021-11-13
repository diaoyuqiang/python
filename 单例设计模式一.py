import threading


class SerialReadWrite(object):
    """
    1.窜口连接:单例模式 请导入单例 不要导入类后实例化 窜口占用只能是一个 跨进程不要导入
    2.基于下位机协议读取窜口原始数据帧
    3.写指令至窜口
    """

    _instance = None
    lock = threading.Lock()  # 获取线程lock

    def __new__(cls, *args, **kwargs):
        """
        无法绝对的避免被多处多次实例化
        窜口无法正常读取时查看被实例化的堆栈信息便于排查问题
        :param args:
        :param kwargs:
        """
        import traceback
        info = traceback.extract_stack()  # 从当前堆栈中获取异常回溯
        if cls._instance:  # 类变量有值返回
            return cls._instance
        else:
            with cls.lock:  # 加锁
                cls._instance = super(SerialReadWrite, cls).__new__(cls)  # 将类的实例绑定到类变量_instance上
                return cls._instance
