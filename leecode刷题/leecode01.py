"""
1.请从标准输入流（控制台）中获取一个正整数 n 和一个数组 A，
数组 A 共含有 n - 1 个整数，n - 1 个整数的范围都在区间 [1,n] 之间（没有重复），
找出区间 [1,n] 范围内没有出现在数组中的那个数，将该数通过 print 语句输出到标准输出流（控制台）。

"""
n = int(input('整数n:'))
A = input('数组N：').split()  # 默认以空格切分字符串，并返回切割后的列表
A = list(map(int, A))  # list列表生成器: 将map返回的可迭代对象转换成列表

A.sort()  # 列表排序
A.append(-1)
print(A)

for i in range(n):
    if A[i] == i + 1:
        continue
    print(i+1)
    break  # 退出循环
