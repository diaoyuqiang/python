from abc import abstractmethod

class A:
    def __init__(self):
        self.dic = {}
        self.run()

    def run(self):
        self.dic['x'] = 15
        self.dic.update(self.parser_base_info())

    @abstractmethod
    def parser_base_info(self):
        return {}


class B(A):
    def __init__(self):
        super(B, self).__init__()
    # 子类实现父类的抽象方法
    def parser_base_info(self):
        data = {"test": 1}
        return data

class C(B):
    def __init__(self):
        super(C, self).__init__()

    # 子类实现父类的抽象方法
    def parser_base_info(self):
        info = super(C, self).parser_base_info()
        info["name"] = "dyq"
        print(self.dic["x"])
        return info

c = C()
print(c.dic)


