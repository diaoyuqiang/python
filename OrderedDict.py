import collections

# collections.OrderedDict(): 元素排序列表
print('\nOrderedDict:')
d4 = collections.OrderedDict()
d4['a'] = 'A'
d4['b'] = 'B'
d4['c'] = 'C'

d5 = collections.OrderedDict()
d5['c'] = 'C'
d5['a'] = 'A'
d5['b'] = 'B'
print(d4 == d5)  # False  存入元素顺序不一致为不同列表
