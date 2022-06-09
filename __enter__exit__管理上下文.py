#!/usr/bin/env python
# with_example02.py

class Sample:
    def __enter__(self):
        return self

    # 用with处理异常: 打印类型，错误内容，回溯
    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()