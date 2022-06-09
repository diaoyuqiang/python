import queue
from queue import Empty
import json

q = queue.Queue()
q.put(json.dumps("first"))
q.put(json.dumps({1:"second"}))
q.put("thread")

"""
Queue先进先出，get()取空和put()塞满都会阻塞

"""

# while True:
#     print(q.get())
#     # print(q.get())
#     # print(q.get())
while True:
    try:
        q.get(block=True, timeout=1)  # 阻塞1秒取队列
    except Empty:  # 如果为空，pass掉，继续取
        pass

