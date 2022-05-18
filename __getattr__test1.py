# __getattr__: 1.对象属性调用重写  2. 定义字典类
class ObjectDict(dict):  # 定义字典类
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)
    # __getattr__: 用于获取对象属性的最后一步处理
    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


class A(object):
    def __init__(self):
        self.a = 1


class Tree(object):
    def __init__(self):
        pass
    def __getattr__(self, item):
        """
        # 重写__getattr__方法，获取A的属性
        """
        if hasattr(a, item):
            return getattr(a, item)
        else:
            print("异常")
            raise Exception("not attribute")


if __name__ == '__main__':
    od = ObjectDict(asf = {'a': 1}, d = True)  # 关键字参数
    print(od.asf, od.asf.a)  # {'a': 1} 1
    print(od.d)  # True

    # 重写getattr方法后获取属性
    a = A()
    t = Tree()
    print(t.a)