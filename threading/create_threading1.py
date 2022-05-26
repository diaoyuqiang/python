import threading


def hi(num):
    return num
    # print('hello %s' % num)


if __name__ == '__main__':
    t = threading.Thread(target=hi, args=(10,))  # 创建线程对象(子线程) Thread-1
    t.start()
    t1 = threading.Thread(target=hi, args=(8,))  # Thread-2
    t1.start()

    print("我是主线程...")  # MainThread

