class Foo:
    x = 1

    def __init__(self, y):
        self.y = y

    def __getattr__(self, item):
        if item.lower() in self.__dict__.keys():
            # print('----> from getattr:你找的【%s】属性不存在' % item)
            return eval('self.' + item.lower())
        else:
            return "can't find attribute"

    def __setattr__(self, key, value):
        print('----> from setattr')
        if type(value) is str:  # 判断v值为字符串类型,才能加入字典
            print('执行设置操作')
            # self.key = value  # 这就无限递归了,你好好想想
            self.__dict__[key] = value.upper()  # 应该使用它 最底层的操作就是在设置对象的属性字典
        else:
            print('必须是str才能加入')

    def __delattr__(self, item):
        print('----> from delattr')
        # del self.item #无限递归了
        # self.__dict__.pop(item)    #同理直接操作字典

    def __getattribute__(self, item):  # 每次访问属性字典都会调用一次
        print("cross getattribute")
        return super().__getattribute__(item)

    def __getitem__(self, key):  # 允许对象键值取值
        print("first")
        return self.__getattribute__(key)


f1 = Foo('asdfgh')
print(f1.__dict__)
print(getattr(f1, 'y'))  # 获取对象属性都会通过__getattribute__方法
# print(f1["y"])
# print(getattr(f1,'y'))
# print(getattr(f1,'aa'))
