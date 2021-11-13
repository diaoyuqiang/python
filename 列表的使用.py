from functools import reduce
import time
a = [1, 2, 3, 4, 5]

# # 对给定列表中，奇数元素加一，偶数元素加二
# for idx, val in enumerate(a):
#     if val % 2 == 0:
#         a[idx] = val + 2
#     elif val % 2 == 1:
#         a[idx] = val + 1
# print(a)

# a.append('a')  # 向列表末尾添加元素

# 删除列表中的元素
# a.remove(2)
# del a[1]
# a.reverse()  # 翻转

# 拼接列表
# b = [6, 7, 8]
# print(a + b)

# a.clear()  # 清空列表
# print(a)

# c = a.copy()  # 复制列表
# print(c)


# 1.filter
def sp(x):
    return not x % 2  # 被2整除


# filter(function, iterable) 序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到filter object。
b = filter(sp, a)
print(list(b))

# 2.map map() 会根据提供的函数对指定序列做映射
c = map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
print(list(c))

# reduce 对参数序列中元素进行累积。
d = reduce(lambda x, y: x+y, [1, 2, 3, 4])
print(d)


#  [1, 2, 3]变成123
def re(x, y):
    return x * 10 + y


f = reduce(re, [1, 2, 3])
print(f)


# 5、按年龄降序  sorted(iterable[, cmp[, key[, reverse]]])
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(students, key=lambda s: s[2], reverse=True)  # 年龄逆序
print(students)

a = lambda *args: sum(args)  # lambda匿名函数求和
print(a(2, 3))


# 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换
time.sleep = lambda x: None
time.sleep(3)