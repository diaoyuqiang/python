a, b = [3, 2, 1], [6, 9]

# 两个列表元素合并成一个列表
# map(func, *iterables)
lis = list(map(lambda x0, x1: f'{x0}-{x1}', a, b))
print(lis)


# iter(object)返回迭代器
lis = {'na': 12, 'key': "dyq"}
a = iter(lis.items())  # 二元元祖迭代器
for i in a:
    print(i)