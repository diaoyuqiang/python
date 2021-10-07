import queue

q = queue.LifoQueue()
q.put("first")
q.put("second")
q.put("thread")

"""
LifoQueue后进先出
"""

while True:
    print(q.get())
    print(q.get())
    print(q.get())