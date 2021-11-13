from math import pi  # π


class Circle(object):
    def __init__(self, r):
        self.r = r

    # 类方法伪装成属性，不用传参，需要返回值
    @property
    def perimeter(self):
        return 2 * pi * self.r  # 周长

    # 类方法伪装成属性，不用传参，需要返回值
    @property
    def area(self):
        return self.r ** 2 * pi  # 面积


ro = Circle(5)
print(ro.perimeter)  # 相当于访问对象属性
print(ro.area)
