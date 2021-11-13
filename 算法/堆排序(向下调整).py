import random


# 堆排序的调整函数
def sift(li, low, hight):
    """

    :param li:  列表
    :param low: 堆的根节点位置
    :param hight: 堆的最后元素位置
    :return:
    """
    i = low  # 最开始指向根节点
    j = 2 * i + 1  # j为左孩子的位置
    tmp = li[low]  # 把堆顶存起来
    while j <= hight:  # 只要j有位置
        if j + 1 <= hight and li[j+1] > li[j]:  # 如果右孩子比较大
            j = j + 1  # j指向右孩子的位置
        if li[j] > tmp:
            li[i] = li[j]  # 把j位置的元素存入i
            i = j  # i指向下一层
            j = 2 * i + 1
        else:
            li[i] = tmp  # tmp大，把tmp放到i的位置
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点的位置


# 建堆
def heap_sort(li):

    n = len(li)
    for i in range((n-2) // 2, -1, -1):  # i为建堆过程中调整部分的根坐标
        sift(li, i, n-1)  # 建堆完成
# 堆排序
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]  # 交换堆顶和最后一个元素的位置
        sift(li, 0, i-1)   # 调整交换后的堆的位置


li = [n for n in range(100)]
random.shuffle(li)
heap_sort(li)
print(li)




