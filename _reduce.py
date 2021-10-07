# 3.把序列 [1, 3, 5, 7, 9] 变换成整数 13579
from functools import reduce  # 通过函数对指定的序列做累积


def fn(x, y):
    return x * 10 + y


result = reduce(fn, [1, 3, 5, 7, 9])
print(result)
