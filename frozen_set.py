set1 = {1,2,3}
print(type(set1))
set2 = {1,2}

print(set2.issubset(set1))  # set2是否是set1的子集
print(set1.union(set2))  # 并集
print(set1.intersection(set2))  # 交集
print(set1.difference(set2))  # 差集

set1.add(4)  # set添加元素
print(set1)
set1.remove(1)  # set删除元素
print(set1)

# 不可变set
# fset = frozenset([1,2,3])
# fset.add(4)