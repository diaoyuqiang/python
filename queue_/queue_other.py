import queue

q = queue.PriorityQueue()
q.put((2, 'first'))
q.put((3, 'second'))
q.put((1, 'three'))

# q.put(block=False)  # 相当于q.put_nowait(): 队满报错，不阻塞

# 队列的方法
print(q.qsize())  # 队列大小
print(q.full())  # 队列是否已满 True|False
print(q.empty())  # 队列是否为空 True|False

while True:
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get(block=False))  # 相当于q.get_nowait(): 队空抛异常，不阻塞; timeout参数: 超时抛异常