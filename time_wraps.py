from functools import wraps
import time

now = time.time

# 测试函数执行时间的装饰器
def fn_timer(fn=None, *, prefix=""):
    """
    计算 fn 的运算时间

    :param fn: 函数
    :param prefix:
    :return:
    """
    if fn is None:
        return

    @wraps(fn)
    def function_timer(*args, **kwargs):
        start = now()
        result = fn(*args, **kwargs)
        t = now() - start
        if t > 0.002:
            print(f'{prefix}{fn.__name__} total running time {now() - start} seconds')
        return result

    return function_timer


def test():
    for i in range(10):
        time.sleep(1)

fun = fn_timer(test)
fun()