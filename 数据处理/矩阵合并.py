import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

# 矩阵合并
c = np.vstack((a, b))  # 上下合并
print(c)

e = a.reshape((3, 1))  # 将 [1 1 1] 变成3行一列的矩阵
f = b.reshape((3, 1))

d = np.hstack((e, f))  # 左右合并
print(d)