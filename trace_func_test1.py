import sys
import inspect


class Tracer:

    def dump(self, frame, event, arg):
        code = frame.f_code
        module = inspect.getmodule(code)  # 获取代码的模块
        module_name = ""
        module_path = ""
        if module:
            module_path = module.__file__  # 模块路径
            module_name = module.__name__  # 模块名称: __main__
        print(event, module_path, module_name, code.co_name, frame.f_lineno, frame.f_locals, arg)  # f_locals: 函数调用时得参数信息

    def trace(self, frame, event, arg):
        self.dump(frame, event, arg)
        return self.trace

    def collect(self, func, *args, **kwargs):
        sys.settrace(self.trace)
        func(*args, **kwargs)
        sys.settrace(None)


def add(a, b):
    c = 2
    d = 3
    e = c + d
    return a + b + e


if __name__ == "__main__":
    t = Tracer()
    t.collect(add, 1, 2)
    # print(add(1, 2))


