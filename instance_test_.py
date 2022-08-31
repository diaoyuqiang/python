import copy

class ParamsName:
    """
    参数名（中英文就行）
    之后可使用多语言包添加多语言
    """

    def __init__(self, en, cn):
        self.en = en.strip()
        self.cn = cn.strip()

class Tree():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.name = ParamsName("admin", "dyq")  # 实例属性为另一个基础类的obj

    def to_dict(self):
        ins = copy.deepcopy(self)
        dict_data = ins.__dict__
        dict_data["name"] = ins.name.__dict__  # 基础类的属性字典
        print(dict_data)

t = Tree()
t.to_dict()