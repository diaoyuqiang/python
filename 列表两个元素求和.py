a = [1, 2, 3, 4, 7, 9, 5]


# 1.输出列表中任意两个元素之和等于给定值的元素 O(n2)
def add(li, val):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if val == a[i] + a[j]:
                return i, j
    return None


c = add(a, 16)
print(c)


# 2.a = sum - b 字典保存元素和索引 O(n)
def sum_of_two(arr, target):
    dic = {}
    for i, x in enumerate(arr):
        j = dic.get(target-x, -1)
        if j != -1:
            return j, i
        else:
            dic[x] = i

    return None


d = sum_of_two(a, 17)
print(d)

