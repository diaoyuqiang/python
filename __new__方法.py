# __new__: 必须有返回值，返回实例化出来的实例，可以return父类new出来的实例，或直接是object的new出来的实例。
class Dog(object):
    def __init__(self):
        self.name = "旺财"
        print(self.name)


class Person(object):

    def __init__(self):
        self.name = "张三"
        print("__init__")

    def __new__(cls):
        print('__new__')
        ob = object.__new__(Dog)  # ob为Dog类对象
        ob.__init__()
        return ob


p1 = Person()
# print(type(p1))  # 为Dog类的实例对象
# print(p1.name)


# class Person(object):
#     
#     def __init__(self):
#         print("__init__")
#         self.name="张三"
#         
#     def __new__(cls):
#         print('__new__')
#         ob = object.__new__(cls)#ob为Person实例对象
#         print(ob)
#         return ob
#     
#     
# p2 = Person()
# print(p1.name)
