import contextlib


# 上下文管理器
@contextlib.contextmanager
def run():
    for i in range(10):
        print(i)
    try:
        yield  # yield: 将函数分成两部分，yield之前的先在with run()中执行，yield之后的代码，在with代码块结束后执行。
    finally:
        print("执行完毕")


with run():
    print('center states')