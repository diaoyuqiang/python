# encoding=utf-8
# 迭代器、生成器、可迭代对象 详解见视频：https://www.bilibili.com/video/BV1BT4y1P7nn?from=search&seid=10353610141994125966
# 0到100偶数列表
li = [i for i in range(0, 101) if i % 2 ==0]
print(li)

# 1.生成器表达式
l2 = (i for i in range(0, 101) if i % 2 ==0)
print(l2)
print(next(l2))
print(next(l2))
print(l2.__next__())

# 2.生成器函数
# yield 可以阻断当前函数的执行，下次调用next函数时会继续执行，执行到下个yield为止，并返回yield 后面的值。
def test():
    print("01")
    yield 1

    print("02")
    print('a')

    yield 2
    print('b')

    yield 3
    print('c')

    yield 4
    print('d')

q = test()
print(q)
print(next(q))
print(q.__next__())

# send 方法给上个yield赋值，如果没有上个yield，可传None
def text():
    print("xxx")
    test1 =yield 1
    print(test1)

    test2=yield 2
    print(test2)

g = text()
print(g.__next__())
# print(g.__next__())
print(g.send("ooo"))

# close 关闭生成器
g.close()