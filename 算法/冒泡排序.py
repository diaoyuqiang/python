import random


def bubble_sort(li):
    for i in range(len(li)-1): # 第i趟
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return


list01 = [random.randint(0, 10000) for i in range(1000)]
bubble_sort(list01)
print(list01)
# 冒泡排序

