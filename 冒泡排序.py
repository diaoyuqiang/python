import random


# 列表的冒泡排序O(n2)
def bubble_sort(li):
    for i in range(len(li)-1):  # 冒泡次数
        exchange = False
        for n in range(len(li)-i-1):  # 第n趟要遍历的无序区
            if li[n] > li[n+1]:
                li[n], li[n+1] = li[n+1], li[n]
                exchange = True  # 每一次遍历无序区判断下是否交换

        if not exchange:  # 无交换表示已排好序
            return


lis = [random.randint(1, 1000) for i in range(100)]
print(lis)
bubble_sort(lis)
print(lis)