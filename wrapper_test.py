import functools

def request_retry(times):
    """
    http请求重试
    :params: times 重试次数
    :params: wait_time 重试间隔
    """
    def middle_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            for i in range(times):
                res = func(*args, **kwargs)
                if res:
                    return res
                else:
                    print("error")
        return inner_wrapper
    return middle_wrapper

func = request_retry(3)

# @func
def test(n):
    print(n)
    pass

func(test)(4)