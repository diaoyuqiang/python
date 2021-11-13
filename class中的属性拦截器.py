class A(object):
    def __init__(self, name):
        self.name = name

    # 访问不存在的属性时，先访问__getattribute__，后调用__getattr__， 对不存在的属性进行操作
    def __getattr__(self, attr):
        return eval("self." + attr.lower())  # 即：再次去执行__getattribute__方法

    # 属性拦截器__getattribute__(self, item), 必须有返回值，继承自object的类都有此方法
    def __getattribute__(self, item):
        return super().__getattribute__(item)


if __name__ == "__main__":
    a = A('小白')
    print("a.name -> {}".format(a.name))
    print("a.NAME -> {}".format(a.NAME))
