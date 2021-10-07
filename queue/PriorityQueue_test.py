import queue

q = queue.PriorityQueue()
q.put((2, 'first'))
q.put((3, 'second'))
q.put((1, 'three'))

"""
PriorityQueue指定出队优先级

"""

while True:
    print(q.get())
    print(q.get())
    print(q.get())