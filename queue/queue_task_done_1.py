import threading
import queue
import time

q = queue.Queue()
"""
    Queue 模块中的 task_done , join
    一个例子解决;
    这个例子将阻塞
    task_done : 用于 get 的后续调用.告诉队列任务处理完成.当然你也可以不调用get
    join: 阻塞操作,直到队列所有的任务都处理. 
          大白话是你往里 put 几次,就要调用task_done几次,自己可以试下
"""


def worker(q):
    time.sleep(0.5)
    item = q.get()  # 获取
    print('{} get {} , {} left'.format(threading.currentThread().ident, item, q.qsize()))  # 获取当前线程的id
    q.task_done()  # 任务处理完成


for i in range(4):  # 创建4个线程去获取
    t = threading.Thread(target=worker, args=(q,))
    t.start()

for i in range(5):
    # chr()返回对应的ascii码
    q.put([chr(i), i])  # 入队5个
print('main thread running')
# for i in range(5):            #你也可以这么玩
#     q.task_done()
q.task_done()
q.join()  # 阻塞,直到调用5次task_done

if q.all_tasks_done:
    print("okk")
print('main thread end')