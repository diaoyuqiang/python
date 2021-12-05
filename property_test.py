# property函数用法
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    # property: 返回属性值得方法  | 获取属性值、设置属性值、删除属性；属性描述信息
    x = property(getx, setx, delx, "I'm the 'x' property.")


a = C()
print(a.x)
a.x = 1
print(a.x)
del a.x


# # 装饰器用法
# class Parrot(object):
#     def __init__(self):
#         self._voltage = 100000
#
#     @property
#     def voltage(self):
#         """Get the current voltage."""
#         return self._voltage