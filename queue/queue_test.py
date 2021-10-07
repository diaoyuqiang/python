import queue

q = queue.Queue()
q.put("first")
q.put("second")
q.put("thread")

"""
Queue先进先出，get()取空和put()塞满都会阻塞

"""

while True:
    print(q.get())
    print(q.get())
    print(q.get())
