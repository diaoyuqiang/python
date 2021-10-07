# 1.map(function, iterable, ...) --根据函数对序列做映射，并返回可迭代对象。
def square(x):
    return x ** 2


# 列表生成器: 将map返回的可迭代对象转换成列表
q = list(map(square, [1, 2, 3, 4, 5]))
print(q)


# 2.join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
s = "-"
agg = {"r", "u", "n", "o", "o", "b"}  # 集合为无序不重复的序列，用set()创建{}
print(s.join(agg))  # str.join(序列) 以str作为序列的连接符。

# 3.集合的基本操作
a = {x for x in 'abbddggwcc' if x not in 'bdg'}  # 遍历字符串,并且无序不重复
print(a)

# 下面展示两个集合间的运算.

a = set('abracadabra')
b = set('alacazam')

c = a - b  # 集合a中包含而集合b中不包含的元素
c2 = a | b  # 集合a或b中包含的所有元素
c3 = a & b  # 集合a和b中都包含了的元素
c4 = a ^ b  # # 不同时包含于a和b的元素

a.add('x')
a.update('x')  # 添加元素

a.remove('x')
# a.discard()  # 移除元素

