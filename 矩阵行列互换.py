import numpy as np

# 1.数组实现行列转换
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(list(map(list, zip(*a))))

# 2.利用numpy实现矩阵的行列转换(转置)
print(np.transpose(a))

# a = [1, 2, 3]
# b = [4, 5, 6]
# list1 = [(1, 2), (3, 4), (5, 6)]
#
# print(list(map(list, zip(*list1))))
