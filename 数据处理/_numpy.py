import numpy as np  # 维度数组与矩阵运算

array = np.array([[1, 2, 3],
                  [2, 3, 4]], dtype=float)

print(array)
print('维度dimension：', array.ndim)
print('形状shape:', array.shape)
print('矩阵大小size:', array.size)
print('矩阵类型', array.dtype)
# np.matrix: 创建新的矩阵 np.matrix().I: inverse(矩阵反转，数值*(-0.5))
print(np.matrix(np.array([[1,2],
                [3, 4]])).I)

# a = np.zeros((3, 4), dtype=int)  # 元素为0的三行四列数组
# print(a)
#
# b = np.arange(0, 10, 2)  # 0-8一维数组
# print(b)
#
# c = np.arange(12).reshape((3, 4))  # 0-11三行四列数组
# print(c)
#
# d = np.linspace(1, 10, 6).reshape((2, 3))  # 1-10平均分段6份，输出两行三列的数组
# print(d)
a = np.matrix(np.array([[1,2],
                [3, 4]])).I

print(np.sqrt(array))