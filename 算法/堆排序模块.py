import heapq  # 堆排序模块 q->queue 优先队列
import random

li = list(range(100))
random.shuffle(li)
print(li)

# 建小根堆
heapq.heapify(li)
print(li)

# heappop 每次取堆的最小值
n = len(li)
for i in range(n):
    print(heapq.heappop(li), end="")
