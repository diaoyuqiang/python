from collections.abc import Mapping, MutableSequence
# dict继承自Mapping(映射); list继承自MutableSequence(可变序列)

# dic = {}
# print(isinstance(dic, Mapping))
# lis = []
# print(isinstance(lis, MutableSequence))

class AttrError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "对象不存在 {} 属性，请仔细检查".format(self.msg)

class MessageJSON():
    """
    一个只读接口，使用属性表示法访问JSON类对象
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):  # hasattr只作用于对象
            return getattr(self.__data, name)  # getattr只作用于对象
        else:
            try:
                return MessageJSON.build(self.__data[name])
            except AttributeError:
                raise AttrError(name)

    @classmethod
    def build(cls, obj):
        if isinstance(obj, Mapping):
            return cls(obj)  # 返回对象，通过属性方法读取
        elif isinstance(obj, MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


d1 = {"a":"1", "b":{"c":1, "d":[1, 2, [3, 4]]}}
f = MessageJSON(d1)
print(f.b.c)
# print(isinstance([1,2,2], MutableSequence))