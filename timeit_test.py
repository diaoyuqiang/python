# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/10/11

import timeit


# 待测试的函数
def add():
    return sum(range(111))


# stmt 需要测试的函数或语句，字符串形式
# setup 运行的环境，本例子中表示 if __name__ == '__main__':
# number 被测试的函数或语句，执行的次数，本例表示执行100000次add()。省缺则默认是10000次
# repeat 测试做100次
# 综上：此函数表示 测试 在if __name__ == '__main__'的条件下，执行100000次add()消耗的时间，并把这个测试做100次,并求出平均值

t = timeit.repeat(stmt="add()", setup="from __main__ import add", number=100000, repeat=100)  # 加入repeat参数后，返回时间列表
print(t)
print(sum(t) / len(t))