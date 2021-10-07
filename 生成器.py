# 迭代器、生成器、可迭代对象 详解见视频：https://www.bilibili.com/video/BV1BT4y1P7nn?from=search&seid=10353610141994125966

# 0到100偶数列表
li = [i for i in range(0, 101) if not i % 2]  # python中默认0为False,所以：not i % 2 == True(取偶数)
print(li)

# 1.生成器表达式
l2 = (i for i in range(0, 101) if i % 2 == 0)
print(l2)
print(next(l2))
print(l2.__next__())

# 2.生成器函数
# yield 可以阻断当前函数的执行，下次调用next函数时会继续执行，执行到下个yield为止，并返回yield 后面的值


def test():
    print("01")
    yield 1

    print("02")
    print('a')
    yield 2

    print('b')
    yield 3

    print('c')
    print('d')
    yield 4


q = test()  # 根据内部generator类生成的q生成器对象，生成器类中包含__iter__, __next__方法
print(dir(q))
print(next(q))
print(q.__next__())


def text():  # send 方法给上个yield赋值，如果没有上个yield，可传None
    print("xxx")
    test1 = yield 1
    print(test1)

    print('2次')
    test2 = yield 2


g = text()
print(g.__next__())
# print(g.__next__())
print(g.send("测试"))

# close 关闭生成器
g.close()