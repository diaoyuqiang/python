import queue
import time
import threading

q = queue.Queue()


def put():
    while True:
        q.put("first")
        q.put("second")
        q.put("three")
        time.sleep(3)


def get():
    while True:
        print(q.get())
        print(q.get())
        print(q.get())


if __name__ == '__main__':
    t = threading.Thread(target=put)
    t1 = threading.Thread(target=get)
    t.start()
    t1.start()
