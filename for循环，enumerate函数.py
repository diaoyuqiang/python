# 普通for循环打印列表索引和值
i = 0
seq = ["one", "two", "three"]
for ele in seq:
    print("%d .. %s" % (i, ele))
    i += 1

# enumerate函数打印列表索引和值
seq = ["one", "two", "three"]

for i, ele in enumerate(seq):
    print("%d .. %s" % (i, ele))

# for循环拼接字符串
list1 = ["01", "02", "03"]
list1 = ["1" + str for str in list1]
print(list1)