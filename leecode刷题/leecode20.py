"""
给定一个数组 A，数组 A 共含有 n 个整数，计算数组 A 内所有整数的和。
"""

array = list(map(int, input().split()))
print(sum(array))  # sum函数对可迭代的对象求和