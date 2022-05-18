import numpy as np

# # 一维矩阵运算
# a = np.array([10, 20, 30])
# b = np.arange(3)
#
# c = a - b
# c1 = a * b
# print(c)
# print(c1)
# # 判断b数组中元素的大小
# print(b < 2)

a = np.array([[1, 1],
              [2, 3]])
b = np.arange(4).reshape(2, 2)
print(a)
print("b:", b)
print('*' * 50)
# c = a * b  # 元素相乘
# 矩阵相乘的条件: 第一个矩阵的列数等于第二个矩阵的行数
c_dot = a.dot(b)  # 矩阵相乘(前行乘后列)
c2 = np.dot(a, b)

# # print(c)
print(c2)
print(c_dot)

# 0-1两行四列的随机矩阵
d = np.random.random((2, 4))
print(d)

print(np.sum(d))  # 矩阵元素和
print(np.min(d, axis=1))  # 每一行中的最小值
print(np.max(d, axis=0))  # 每一列中的最大值

A = np.arange(2, 14).reshape((3, 4))
print(np.argmin(A))  # 打印最小值的索引
print(A.mean())  # 矩阵A的平均值
print(np.cumsum(A))  # 累加数组中的元素
print(np.sort(A))  # 排序
print(np.transpose(A))  # 行列转化
print(np.clip(A, 5, 9))  # 矩阵元素大小区间5-9

# 数组索引
B = np.arange(3, 15).reshape((3, 4))
print(B[1, 1])  # 第一行第一列的元素
print(B[1, 1:3])  # 第一行一到三列的元素
# print(B.T)  # 矩阵转置
for col in B.T:
    print(col)

# print(B.flatten())  # 将数组中的元素放到一个list中
for item in B.flat:
    print(item)