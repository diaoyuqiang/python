from multiprocessing import Process
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

    t = Process(target=listen)  # 创建子进程
    # print(t.daemon)
    t.daemon = True  # 设置该进程为守护进程，必须放在start之前,主进程执行完后，t也结束
    t.start()  # 启动进程活动

    t1 = Process(target=game)  # 创建子进程
    t1.daemon = True  # 设置该进程为守护进程，必须放在start之前,主进程执行完t1结束
    t1.start()

    # t.join()  # 阻塞t进程，在t进程执行完之前它的主进程会被阻塞
    print('这是主进程......')