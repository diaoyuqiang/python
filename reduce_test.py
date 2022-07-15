from functools import reduce

"""
reduce函数先从列表（或序列）中取出2个元素执行指定函数，并将输出结果与第3个元素传入函数，输出结果再与第4个元素传入函数，…，以此类推，直到列表每个元素都取完。
"""
# 0 1 2 3
lis = [i for i in range(4)]
# print(reduce(lambda x, y: x if (x+y)/2 ==0 else y, lis))


a = 3

if a == 1:
    print("1")
elif a == 2 or a == 1:
    print("1, 2")

elif a == 3:
    print("3")