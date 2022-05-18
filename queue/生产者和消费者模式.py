import queue, threading
import time

# 获取线程函数返回值的两种方法: 1.线程类定义获取函数; 2.放进队列里
q = queue.Queue()  # 线程队列对象（生产者和消费者模式）


# 生产者
def producer(name):
    count = 1
    # 生产10个包子
    while count <= 10:
        print('%s准备制作第%s个包子' % (name, count))
        time.sleep(0.5)
        q.put(count)  # 放入线程队列
        print('制作成功！')
        count += 1


# 消费者
def consumer(name):
    count = 1
    # 吃包子
    while count <= 10:
        time.sleep(1)
        # if not q.empty():
        print('%s准备吃第%s个包子' % (name, count))
        q.get()
        q.task_done()
        # else:
        #     print('暂时没有包子请稍等')
        count += 1


if __name__ == '__main__':
    T1 = threading.Thread(target=producer, args=('厨师A', ))
    T2 = threading.Thread(target=consumer, args=('B客户', ))
    T1.start()
    T2.start()
    time.sleep(1)
    q.join()
    print("main end")
    # print(q.get())  #主线程取出第一个包子，'B客户'暂时没有包子吃