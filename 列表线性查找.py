list1 = [1, 2, 4, 5]


# 列表顺序查找(线性查找) O(n)
def linear_search(li, var):
    for i, vo in enumerate(li):
        if vo == var:
            return i
    else:
        return None


a = linear_search(list1, 2)
print(a)