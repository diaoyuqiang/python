# 1.选择排序
def select_simple(li):
    min_list = []
    for i in range(len(li)):
        min_val = min(li)
        min_list.append(min_val)
        li.remove(min_val)
    return min_list


# 2.选择排序 O(n2)
def select_sort(li):
    for i in range(len(li)-1):  # 要遍历的次数
        min_idx = i  # 记录有序区最后一位索引
        for j in range(i+1, len(li)):  # 无序区的位置
            if li[j] < li[min_idx]:
                min_idx = j  # 无序区最小数的索引位置设置为min_idx
        li[i], li[min_idx] = li[min_idx], li[i]  # 替换有序区最后一位


lis = [2, 6, 3, 1, 9]
select_sort(lis)
print(lis)

