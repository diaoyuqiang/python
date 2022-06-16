import threading
import time


def listen():
    print('start to listen music..%s' % time.strftime('%X'))
    time.sleep(3)
    print('end to listen music..%s' % time.strftime('%X'))


def game():
    print('begin to game %s' % time.strftime('%X'))
    time.sleep(5)
    print('end to game %s' % time.strftime('%X'))


if __name__ == '__main__':

    t = threading.Thread(target=listen)  # 创建子线程
    t.setDaemon(True)  # 设置该线程为守护线程，必须放在start之前
    t.start()  # 启动线程活动
    print("线程名称:", t.name)  # 查看线程名称
    # print(t.is_alive())  # 检查线程是否活动
    # print(t.getName())  # 返回线程名称
    # t.setName("我是线程1")  # 设置线程名称
    # print(t.getName())

    print(threading.enumerate())  # 返回正在运行的线程列表
    print(threading.currentThread().name)  # 返回当前线程名称
    print(threading.get_ident())  # 返回线程id
    print(threading.active_count())  # 查看正在运行的线程数量

    t1 = threading.Thread(target=game)  # 创建子线程
    t1.setDaemon(True)  # 设置该线程为守护线程，必须放在start之前,主线程执行完t1结束
    t1.start()

    # t.join()  # 阻塞t线程，在t线程执行完之前它的主线程会被阻塞
    print('这是主线程......')