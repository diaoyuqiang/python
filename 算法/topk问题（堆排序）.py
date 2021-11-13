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
        if j + 1 <= hight and li[j+1] < li[j]:  # 如果右孩子比较大
            j = j + 1  # j指向右孩子的位置
        if li[j] < tmp:
            li[i] = li[j]  # 把j位置的元素存入i
            i = j  # i指向下一层
            j = 2 * i + 1
        else:
            li[i] = tmp  # tmp大，把tmp放到i的位置
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点的位置


# 取前k大的数
def topk(li, k):
    heap = li[0:k]
    # 1.建堆
    for i in range((k-2) // 2, -1, -1):
        sift(heap, i, k-1)
    # 比较li中k往后的元素与堆顶
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)  # 加入heap并调整heap堆的顺序
    # 挨个输出
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]  # 交换堆顶和最后一个元素的位置
        sift(heap, 0, i-1)   # 调整交换后的堆的位置
    return heap


li = list(range(1000))
random.shuffle(li)
var = topk(li, 10)
print(var)