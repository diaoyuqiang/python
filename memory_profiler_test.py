from memory_profiler import profile


class A(object):  # 没有定义__slots__属性
    # __slots__ = ('x')
    a = 1
    def __init__(self, x):
        self.x = x


@profile  # 跟踪函数使用的内存情况
def main():
    f = [A(i) for i in range(10000)]


if __name__ == '__main__':
    main()

