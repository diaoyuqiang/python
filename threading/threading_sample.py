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
    # t.setDaemon(True)  # 设置该线程为守护线程，必须放在start之前
    t.start()

    t1 = threading.Thread(target=game)  # 创建子线程
    # t1.setDaemon(True)  # 设置该线程为守护线程，必须放在start之前,主线程执行完t1结束
    t1.start()

    t.join(timeout=1)  # 在t线程执行完之前它的主线程会被阻塞 | timeout=1 参数：t线程超时1秒后主线程直接执行
    print('这是主线程......')