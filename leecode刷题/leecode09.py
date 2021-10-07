"""
[5, 6, 9, 8]
[1, 0, 7, 6]
列表合并排序
"""

dt1 = [5, 6, 9, 8]
dt2 = [1, 0, 7, 6]


def merge(li, li1):
    li.extend(li1)  # 列表合并
    li.sort()  # 列表排序
    return li


result = merge(dt1, dt2)
print(result)