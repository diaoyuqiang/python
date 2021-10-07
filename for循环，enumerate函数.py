# 普通for循环打印列表索引和值
i = 0
seq = ["one", "two", "three"]
for ele in seq:
    print("%d .. %s" % (i, ele))
    i += 1

# enumerate枚举函数 打印列表索引和值
for i, ele in enumerate(seq, start=1):  # enumerate先打印索引，后打印序列的值 | start: 索引开始值
    print("%d : %s" % (i, ele))

# for循环拼接字符串列表
list1 = ["01", "02", "03"]
list1 = ["1" + _str for _str in list1]
print(list1)