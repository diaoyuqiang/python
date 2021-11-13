list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]  list分组


def new_list(lis: list) -> list:
    od = []
    for idx, val in enumerate(lis):
        if len(lis) % 3 == 0:
            if val % 3 == 0:
                od.append(lis[idx - 2: idx + 1])
        else:
            if val % 3 == 0:
                od.append(lis[idx-2: idx+1])
            elif val % 3 != 0 and val in lis[-2:]:
                od.append(lis[idx:])
                break
    return od


a = new_list(list1)
print(a)

