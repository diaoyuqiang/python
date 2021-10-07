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
    t.start()

    t1 = Process(target=game)  # 创建子进程
    t1.start()

    t.join(timeout=1)  # 在t进程执行完之前它的主进程会被阻塞 | timeout=1 参数：t进程超时1秒后主进程直接执行
    print('这是主进程......')