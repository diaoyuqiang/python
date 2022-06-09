# coding=utf-8
from queue import Empty, Queue
from threading_ import Thread, Lock


class Event(object):
    """事件"""

    def __init__(self, event_type=None):
        self.event_type = event_type  # 类型
        self.dict = {}  # 数据
        # self.mutex = Lock()  # 锁


class EventManager(object):
    """事件管理器"""

    STOP_EVENT = object()

    def __init__(self):
        # 事件对象队列
        self.__eventQueue = Queue()
        # 事件处理线程
        self.__thread = Thread(target=self.__run)
        # 事件处理字典，用来保存对应的事件的响应函数，一对多{'event1': [handler1,handler2] , 'event2':[handler3, ...,handler4]}
        self.__handlers = {}

    def __run(self):
        """执行事件循环"""
        while True:
            try:
                event = self.__eventQueue.get(block=True, timeout=1)
                self.__event_process(event)
                if event.event_type == EventManager.STOP_EVENT:
                    break
            except Empty:
                pass

    def __event_process(self, event):
        """依次执行注册的处理函数"""
        if event.event_type in self.__handlers:
            # 顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.event_type]:
                handler(event)

    def start(self):
        """启动"""
        self.__thread.start()

    def stop(self):
        """停止"""
        stop_event = Event(EventManager.STOP_EVENT)
        self.send_event(stop_event)
        self.__thread.join()

    def register_handler(self, event_type, handler):
        """注册事件handler"""
        try:
            handler_list = self.__handlers[event_type]
        except KeyError:
            handler_list = []
            self.__handlers[event_type] = handler_list

        if handler not in handler_list:
            handler_list.append(handler)

    def unregister_handler(self, event_type, handler):
        """注册事件handler"""
        try:
            handler_list = self.__handlers[event_type]
            if handler in handler_list:
                handler_list.remove(handler)

            if not handler_list:
                del self.__handlers[event_type]
        except KeyError:
            pass

    def send_event(self, event):
        """发送事件"""
        # 加入队列
        self.__eventQueue.put(event)


if __name__ == '__main__':
    import time

    EVENT_ERROR = "event_error"

    # 事件源
    class Agv:
        def __init__(self, event_manager):
            self.__event_manager = event_manager

        def event_error(self):
            event = Event(EVENT_ERROR)
            event.dict["error"] = 'agv error occurred'
            # 发送事件
            self.__event_manager.send_event(event)
            print('agv 发出异常事件')

    # 处理器1
    class Handler1:
        def __init__(self, username):
            self.__username = username

        # 处理函数
        def handle_error(self, event):
            print('%s 收到异常信息：%s' % (self.__username, event.dict))

    # 处理器1
    class Handler2:
        def __init__(self, username):
            self.__username = username
            self.__queue = Queue()
            self.__thread = Thread(target=self.__run)
            self.__thread.start()

        # 处理函数
        def handle_error(self, event):
            print('%s 收到异常信息：%s' % (self.__username, event.dict))
            self.__queue.put(event)

        def __run(self):
            while True:
                try:
                    event = self.__queue.get(block=True, timeout=1)
                    if event.event_type != EventManager.STOP_EVENT:
                        print('%s 新起的线程处理event：%s' % (self.__username, event.dict))
                    else:
                        print('%s 新起的线程处理event：%s' % (self.__username, '停止事件'))
                        break
                except Empty:
                    pass


    handler1 = Handler1("one")
    handler2 = Handler2("two")

    em = EventManager()

    em.register_handler(EVENT_ERROR, handler1.handle_error)
    em.register_handler(EVENT_ERROR, handler2.handle_error)
    em.register_handler(EventManager.STOP_EVENT, handler2.handle_error)

    em.start()

    # 发送事件
    agv = Agv(em)
    agv.event_error()

    time.sleep(5)

    print("停止线程处理")
    em.stop()