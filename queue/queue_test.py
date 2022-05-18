import queue
import json

q = queue.Queue()
q.put(json.dumps("first"))
q.put(json.dumps({1:"second"}))
q.put("thread")

"""
Queue先进先出，get()取空和put()塞满都会阻塞

"""

while True:
    print(q.get())
    # print(q.get())
    # print(q.get())
