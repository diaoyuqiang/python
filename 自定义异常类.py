# 自定义消息转化异常类
class MessageConvertException(Exception):  # 继承自Exception
    def __init__(self, error_info):
        super(MessageConvertException, self).__init__()
        self.error_info = error_info

    def __str__(self):
        return "message内部类对象生成出错，请检查传入mapping_path是否正确 报错信息:{}".format(self.error_info)

class Tree(object):
    def __init__(self):
        try:
            # self.a = self.b
            self.a = 1

        except Exception as e:
            # 抛出自定义异常
            raise MessageConvertException(e)


t = Tree()
