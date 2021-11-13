import random


# O(nlogn) - O(n2)
def partition(li, left, right):
    n = random.randint(left+1, right)  # 防止出现O(n2)
    li[left], li[n] = li[n], li[left]
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]  # 找右边比tmp小的值放到左边
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 找左边比tmp大的值放到右边
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 4, 8, 12, 14, 3, 7]
quick_sort(li, 0, len(li) - 1)
print(li)