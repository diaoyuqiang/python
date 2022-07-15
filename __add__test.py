class Model:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):  # 对象相加时调用，return一个对象
        return  Model(self.x+other.x)

    def __sub__(self, other):
        return Model(self.x - other.x)

    def __str__(self):  # 返回一个对象的描述信息
        return ("两个对象相加的值是: {x}".format(x=self.x))

a=Model(5)
b=Model(7)
print(a+b)
print(a-b)
