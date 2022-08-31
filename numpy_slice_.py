import numpy as np
#
# x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
#
# print(x[..., 0])
# print(x[:, :, 0])

sr = 'python'
# 格式：[开头：结束：步长]
# print(sr[::1])
# print(sr[::-1])
#
# lis = [1, 2, 3, 4, 5]
# l1 = lis[2:]
# print('lis:{}, l1:{}'.format(lis, l1))
# print(lis[2::-1])
# print(lis[-2:-4:-1])

a = np.array([[0,1,2,3],
              [4,5,6,7],
              [20,21,22,23],

             [30,31,32,33]])

# 前面是行索引，后面是列索引
print(a[2, 1])
# print(a[0:2, 1:3])
# print(a[:2, :2])
# print(a[:, : 1])  # 取所有维度的index为0的元素
print(a[..., 0:2])  # ...相当于所有::