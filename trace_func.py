# program to display the functioning of
# settrace()
from sys import settrace  # 回溯本质上是代码中发生事件时返回的信息


# local trace function which returns itself
def my_tracer(frame, event, arg=None):
    # extracts frame code
    code = frame.f_code  # 当前堆栈帧

    # extracts calling function name
    func_name = code.co_name  # 当前堆栈调用的函数名称

    # extracts the line number
    line_no = frame.f_lineno  # 代码行号

    print(f"{event} encountered in \
    {func_name}() at line number {line_no} ")

    return my_tracer


# global trace function is invoked here and
# local trace function is set for fun()
def fun():
    return "GFG"


# global trace function is invoked here and
# local trace function is set for check()
def check():
    return fun()


# returns reference to local
# trace function (my_tracer)
settrace(my_tracer)  # # 跟踪堆栈信息(函数调用，函数返回，异常，code_line)

check()
settrace(None)  # 函数执行结束后，停止跟踪