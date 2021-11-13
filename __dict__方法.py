# __dict__: 储存对象属性的字典
class Lic(object):
    def __init__(self, pa_lict):
        self.__dict__.update(pa_lict)  # update: 将字典对象合并到字典中


lic = Lic(para_dc)
a = lic.__dict__['name']

print(a)


"""
a、类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的
b、对象的__dict__中存储了一些self.xxx的一些东西
"""

# 
# class TestName:
#     a = 2
#     b = 2
# 
#     def __init__(self,c):
#         self.a = 0
#         self.b = 1
#         self.c = c
# 
#     def test1(self):
#         print("a normal func")
# 
#     @staticmethod
#     def static_test(self):
#         print("a static class")
# 
#     @classmethod
#     def class_test(self):
#         print("a class func")
# 
# 
# o = TestName(2)
# print(TestName.__dict__)
# print(o.__dict__)
