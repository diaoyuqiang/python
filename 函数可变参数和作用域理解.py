# -*- coding: utf-8 -*-

def mylist(da, lis=[]):
    if lis:
        # print lis, id(lis)
        lis = []
    lis.append(da)
    print(lis, id(lis))


mylist(1)
mylist(2)
mylist(3)

# def run(da, lis=None):  # 函数的默认值参数只会在定义的时候初始化一次
#     # print(id(lis))  # 形参的内存地址
#     if lis is None:
#         lis = []  # 新的列表变量
#     lis.append(da)
#     print(lis, id(lis))
#
# run(1)
# run(2)
