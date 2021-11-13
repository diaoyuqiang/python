list1 = [1, 2, 4, 5, 8, 9, 15]


# 列表的二分查找 O(logn)
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return None


a = binary_search(list1, 8)
print(a)
