# 插入排序
def insert_sort(li):
    for i in range(1, len(li)):  # 要排序的区域
        j = i - 1  # 已排序的最后一位
        temp = li[i]  # 要获取的元素
        while j >= 0 and li[j] > temp:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = temp  # 插入元素


lis = [3, 2, 4, 9, 1]
insert_sort(lis)
print(lis)