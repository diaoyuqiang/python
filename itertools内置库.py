import itertools

# 生成指定step的序列
i = 0
for item in itertools.count(10, 2):
    i += 1
    if i >10: break
    print(item)

# 返回p中任意取r个元素做排列的元组的迭代器
for x in itertools.permutations([1, 2, 3, 4], 3):
    print(x)

# 重复序列中的元素
for c in itertools.cycle('abc'):
    print(c)