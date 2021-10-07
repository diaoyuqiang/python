"""
迭代器
类中定义了__iter__, __next__方法
__iter__返回对象本身，即self
__next__返回下一个数据，如果没有下一个数据，则抛出StopIteration的异常
"""


class It(object):
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == 3:
            raise StopIteration("没有数据，停止迭代")
        return self.count


obj1 = It()  # 迭代器对象
q = obj1.__next__()
q1 = next(obj1)  # next()直接调用__next__
print(q, q1)

obj2 = It()
for q in obj2:  # 首先会执行__iter__方法并获取返回值，然后反复执行next(对象)
    print(q)

"""
可迭代对象
类中定义了__iter__方法且返回一个迭代器对象或者生成器对象，称这个类创建的对象为可迭代对象
"""

# class Fot(object):
#     def __init__(self):
#         self.item = 0
#     def __iter__(self):
#         return 迭代器对象（生成器对象)
# obj = Fot()  可迭代对象
# for i in obi:
#     print(i)

vi = range(100)  # vi是可迭代对象
print(dir(vi))