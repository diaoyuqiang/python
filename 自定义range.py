# 基于迭代器的range
class IterRange(object):  # 迭代器类
    def __init__(self, num):
        self.num = num
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.num:
            raise StopIteration()
        return self.count


class Xrange(object):
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        return IterRange(self.max_num)


obj = Xrange(100)  # 可迭代对象
for i in obj:
    print(i)


# 基于生成器的range
class Xrange(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        count = 0
        while count < self.num:
            yield count  # 返回生成器对象
            count += 1


obj1 = Xrange(100)
for m in obj1:
    print(m)