#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 牛顿法
# positive_num = int(input("输入一个正数:"))
# epsilon = 0.01
# answer = positive_num / 2  # 答案肯定小于这个正数的一半
# numGuess = 0
# while abs(answer ** 2 - positive_num) >= epsilon:
#     answer = abs(answer - abs(answer ** 2 - positive_num) / (2 * answer))  # answer每轮按照比率下降
#     numGuess += 1
# print(numGuess, ' ', answer)
#
#
# # 二分法
# positive_num = int(input("输入一个正数(origin_high):"))
# low = 0  # 最小值
# high = positive_num  # 最大值
# answer = (low + high) / 2  # 定义answer
# numGuess = 0
# epsilon = 0.01
#
# while abs(answer ** 2 - positive_num) >= epsilon:
#     numGuess += 1
#     if answer ** 2 < positive_num:
#         low = answer  # 小了就把low调大
#     else:
#         high = answer  # 大了就把high调小
#     answer = (low + high) / 2  # 夹击寻找答案
# print(numGuess, ' ', answer)


# 不动点迭代法
def calp(n):
    x = n
    x2 = n / 2

    while abs(x - x2) > 0.0001:
        x = x2
        x2 = (x + n / x) / 2  # 不动点迭代计算公式

    return x


print(calp(6))
