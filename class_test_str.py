class Phone(object):
    def __init__(self):
        self.a = 1

    def __repr__(self):  # 返回对象的字符串表达形式，__str__: 对终端用户更友好，对象没定义__str__时，str() 函数默认寻找repr代替。
        return "phone"

p = Phone()

print(p)