import sys

def func1(num1, num2):
        x = num1 * num2
        y = num1 / num2
        return x, y

def func2():
    func1(1, 0)

if __name__ == '__main__':
    try:
        func2()
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()  # 获取堆栈回溯对象
        print("exc_type:",exc_type)  # 存放异常类型(类对象)
        print("exc_value:",exc_value)  # 异常参数(实际的异常对象)
        print("exc_traceback:",exc_traceback)  # 堆栈的回溯对象
