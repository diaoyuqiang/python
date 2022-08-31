# class Base(object):
#
#     __slots__ = ['y', 'x']  # 阻止实例分配属性到__dict__
#
#     def __init__(self):
#         self.y = 'aa'
#         self.x = 'xx'
#
#
# b = Base()
# # print(b.__dict__) # 抛错
# print(b.y)
# print(b.x)


class base(object):
    __slots__ = ('x')  # 实例能访问到的属性
    var = 8

    def __init__(self):
        pass

b = base()
# print(b.__dict__)
b.x = 88  # 添加实例变量
print(b.x)

