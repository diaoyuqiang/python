"""
1.将两个列表里的每个值都分别进行相乘
2.将两个列表里的每个值都分别进行相加
3.将两个列表里的值对应相乘

for循环的列表推导式
"""

list1 = [2, 4, 6]
list2 = [3, 5, 7]


def _list(li, li2):
    print([l1 * l2 for l1 in li for l2 in li2])  # 1.将两个列表里的每个值都分别进行相乘
    print([l1 + l2 for l1 in li for l2 in li2])  # 2.将两个列表里的每个值都分别进行相加
    print([li[i] * li2[i] for i in range(len(li))])  # 3.将两个列表里的值对应相乘


_list(list1, list2)