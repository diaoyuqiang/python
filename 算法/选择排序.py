def select_sort_example(li):
    li_new = []
    for i in range(len(li)):
        min_var = min(li)
        li_new.append(min_var)
        li.remove(min_var)
    return li_new


# 改进后的选择排序
def select_sort(li):
    for i in range(len(li)-1): # 第i趟
        min_d = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_d]:
                min_d = j
        li[i], li[min_d] = li[min_d], li[i]


li = [1, 7, 2, 13, 6]
select_sort(li)
print(li)