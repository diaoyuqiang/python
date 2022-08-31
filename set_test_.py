# set 是一个无序不重复的集合序列
# set存放不可变类型（字符串、数字、元组）

a = set('hello')
# print(a)
a.add('d')  # 向集合中添加元素
print(a)

# update(x),将x添加到集合中，且参数可以是列表、元组、字典等
s = set(('a', 'cc', 'f'))
# 添加字典只能添加不可变的--键
dict_1 = {'name': 'bb', 'age': 'cc', 'f': 11}
s.update(dict_1)  # 更新多值到set
print("添加字典"+str(s))

# s.remove('cc')  # 移除集合中的元素
s.discard('cc')  # 丢弃集合中的元素不报错
s.pop()  # 随机删除集合中的元素
s.clear() # 清空集合
print(s)

"""
交集 & : x&y，返回一个新的集合，包括同时在集合 x 和y中的共同元素。
并集 | : x|y，返回一个新的集合，包括集合 x 和 y 中所有元素。
差集 - : x-y，返回一个新的集合,包括在集合 x 中但不在集合 y 中的元素。
补集 ^ : x^y，返回一个新的集合，包括集合 x 和 y 的非共同元素。
"""

x = set('abc')
y = set('af')
print(x&y)
print(x|y)
print(x-y)
print(x^y)  # 补集: 不同时包含在x,y中的元素

s1 = frozenset('abc')  # 不可变集合
print(s1)