from multiprocessing import Process, Pool
import time, os


def foo(i):
    time.sleep(2)
    print(i)
    print('son:', os.getpid())  # 获取子进程pid
    return 'hello %s' % i


# 回调函数的参数为子进程执行成功的返回值
def bar(args):
    print(args)  # 主进程打印子进程返回的数据
    print('bar:', os.getpid())


if __name__ == '__main__':

    pool = Pool(5)  # 创建一个进程池 最大进程数5  默认为cpu的alu
    print('main:', os.getpid())  # 获取主进程pid

    for i in range(1, 101):
        # pool.apply(func=foo, args=(i,), callback=bar)  # 同步
        # 回调函数就是某个子进程执行成功后再去调用的函数
        pool.apply_async(func=foo, args=(i,), callback=bar)  # 异步

    # close与join的调用顺序是固定的，否则报错
    pool.close()
    pool.join()
    print('end')
