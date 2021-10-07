import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)

b = np.split(a, 3, axis=0)  # 将a按列分割成3组
print(b)

c = np.array_split(a, 3, axis=1)  # 将a按行分割成3组(不等分割)
print(c)

print(np.vsplit(a, 3))  # 纵向分割
print(np.hsplit(a, 2))  # 横向分割

# 矩阵赋值
a1 = a  # 赋值运算，指向同一个内存地址，a改变数值，a1也同时改变
a2 = a.copy()  # 浅拷贝，a改变数值，a2保持不变

a[1, 0] = 15  # 把第一行第零列改成12

print(a1)
print(a2)