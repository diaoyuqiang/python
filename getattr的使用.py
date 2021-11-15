class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


if __name__ == '__main__':
    od = ObjectDict(asf={'a': 1}, d=True)
    print(od.asf)
    print(od.asf.a)
    print(od.d)


# 定义了__getattr__()，当访问object不存在的属性时会调用该方法
# 不定义访问不存在的属性时会报 AttributeError
class Cat(object):

    def __init__(self):
        self.name = "jn"

    def __getattr__(self, item):
        return "tm"


cat = Cat()
print(cat.name)
print(getattr(cat, 'name'))
print("*" * 20)
print(cat.age)
print(getattr(cat, 'age'))


# def dic(**kwargs):
#     dic1 = kwargs
#     return dic1
#
#
# a = dic(ast={'sr': 10}, d=5)
# print(a)
