'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：778463939
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
class A():
    def __init__(self):
        self.name = "dyq"
    def __eq__(self, other):
        return self.name == other

a = A()
print(a == "dyq")


class Item:
    def __init__(self, name, weight):
        self.name = name  # # 判断是否与传入的字符串相等
        self.weight = weight

    def __eq__(self, other):
        # `__eq__` is an instance method, which also accepts
        # one other object as an argument.

        if type(other) == type(self) and other.name == self.name and other.weight == self.weight:
            return True
        else:
            return False


cat_1 = Item('Cat', 5)
cat_2 = Item('Cat', 5)

print(cat_1.__eq__(cat_2))  # should evaluate to True
print(cat_1 == cat_2)  # should also evaluate to True
