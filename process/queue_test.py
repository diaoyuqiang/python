from multiprocessing import Queue, Process
import time


def fot(q):
    print(id(q))
    time.sleep(1)
    q.put('123')
    q.put('iG')


if __name__ == '__main__':

    q = Queue()  # 进程队列对象,实现进程间的通信
    p = Process(target=fot, args=(q, ))  # 创建子进程
    p.start()

    print("主进程")
    print(id(q))
    print(q.get())
    print(q.get())