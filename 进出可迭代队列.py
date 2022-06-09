# coding=utf-8
import abc
import time
import queue
from threading_ import Thread, Lock


class ClosableQueue(queue.Queue):
    """
    可暂停接收消息的队列
    子类实现自己业务相关的 biz_set_iter_return_flag 方法, 实现跳出遍历
    """

    def __init__(self, timeout=0.2):
        queue.Queue.__init__(self)
        self.timeout = timeout  # 单次取队列消息的超时时间
        self.CLOSE = object()  # 代表"关闭"的消息
        self.close_flag = False  # False表示未关闭，此时可以处理队列消息；True表示队列关闭，此时不能存取队列消息
        self.close_time = None  # 队列关闭时间
        self.open_time = int(round(time.time() * 1000000))  # 队列开启时间
        self.lock = Lock()

    def __iter__(self):
        try:
            while self.is_open:
                try:
                    if self.biz_set_iter_return_flag():
                        return
                    item = self.get(timeout=self.timeout)
                except queue.Empty:
                    continue
                if item is self.CLOSE:
                    if self.close_time and self.close_time >= self.open_time:
                        self.close_flag = True
                        return
                    else:  # 如果关闭时间在开启时间之后，则该次关闭有效，否则无效
                        continue
                yield item
        finally:
            if not self.all_tasks_done:
                self.task_done()

    @property
    def is_open(self):
        """
        判断是否可以进行取放操作
        @return: type: bool
        """
        if not self.close_flag:
            return True
        else:
            return False

    def close(self):
        """
        队列放入关闭消息, 取完队列消息后关闭
        """
        self.lock.acquire()
        try:
            if self.close_flag:
                raise ClosedException("queue is closed")
            self.put(self.CLOSE)
            self.close_time = int(round(time.time() * 1000000))  # 微秒级
        finally:
            self.lock.release()

    def open(self):
        """
        队列恢复接收消息
        """
        self.lock.acquire()
        try:
            self.close_flag = False
            self.open_time = int(round(time.time() * 1000000))  # 微秒级
        finally:
            self.lock.release()

    def clean_and_close(self):
        """
        清空队列在的消息并发送关闭消息
        """
        self.lock.acquire()
        try:
            if self.close_flag:
                raise ClosedException("queue is closed")
            self.queue.clear()
            self.put(self.CLOSE)
        finally:
            self.lock.release()

    @abc.abstractmethod
    def biz_set_iter_return_flag(self):
        """
        @return: bool 需要跳出返回True，佛祖额返回False
        """
        return False

    def put(self, item, block=True, timeout=None):
        if self.close_flag:
            raise ClosedException("queue is closed now, please open it before put item")
        return queue.Queue.put(self, item, block, timeout)


class ClosedException(Exception):
    def __init__(self, msg=None):
        self.error_code = "QUEUE_CLOSED"
        super(ClosedException, self).__init__(msg)


class StoppableQueueWorker(Thread):
    def __init__(self, func, in_iter, out_queue):
        """
        @param func: 消息处理函数, 对输入消息进行处理
        @param in_iter: 可迭代对象
        @param out_queue: 输出队列
        """
        super(StoppableQueueWorker, self).__init__()
        self.func = func
        self.in_iter = in_iter
        self.out_queue = out_queue  # type: ClosableQueue

    def run(self):
        for item in self.in_iter:
            result = self.func(item)
            if self.out_queue:
                self.out_queue.put(result)


if __name__ == '__main__':

    class DemoCondition(object):
        def __init__(self, condition):
            self.condition = condition

    class MyClosableQueue(ClosableQueue):

        def __init__(self, return_condition):
            """
            @param return_condition
            """
            ClosableQueue.__init__(self)
            self.return_condition = return_condition # type: DemoCondition

        def biz_set_iter_return_flag(self):
            if self.return_condition.condition:
                return True
            else:
                return False


    demo_condition = DemoCondition(False)
    in_queue = MyClosableQueue(demo_condition)
    out_queue = ClosableQueue()

    def do_work(item):
        print('do work ...{}'.format(item))
        time.sleep(0.75)


    worker2 = StoppableQueueWorker(do_work, in_queue, out_queue)
    worker2.start()
    worker2_1 = StoppableQueueWorker(do_work, in_queue, out_queue)
    worker2_1.start()

    for i in range(10):
        in_queue.put(i)

    time.sleep(2.5)
    print('****************** clean and close ****************')
    in_queue.clean_and_close()
    time.sleep(5.5)

    print('******************** open **************************')
    in_queue.open()
    time.sleep(0.5)

    threads = [
        StoppableQueueWorker(do_work, in_queue, out_queue),
        StoppableQueueWorker(do_work, in_queue, out_queue),
        StoppableQueueWorker(do_work, in_queue, out_queue),
    ]

    for i in range(11, 20, 1):
        in_queue.put(i)

    for thread in threads:
        thread.start()
    print('')
    print('***************** to close **************************')
    in_queue.close()

    print(in_queue.qsize())
    print('*************** set iter flag ***********************')
    demo_condition.condition = True
    time.sleep(0.8)
    demo_condition.condition = False

    for i in in_queue:
        if i < 17:
            print(i)
        else:
            print('break {}'.format(i))
            break

    print('*************** after break once ********************')

    for i in in_queue:
        print(i)