import functools
import threading

lis = {"name": 1, "sex": 2}

# 线程对象装饰器
def thread_maker(func):
    @functools.wraps(func)
    def runner(*args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()
        return t

    return runner


@thread_maker
def run(n):
    print(n)

# 线程对象列表
threadlist = [run(x) for x in lis.keys()]

for t in threadlist:
    t.join()  # 阻塞执行线程