from multiprocessing import Process


def hi(num):
    print('hello %s' % num)


if __name__ == '__main__':
    t = Process(target=hi, args=(10,))  # 创建进程对象(子进程) Process-1
    t.start()
    t1 = Process(target=hi, args=(8,))  # Process-2
    t1.start()

    print("我是主进程...")  # MainProcess

