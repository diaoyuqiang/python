from multiprocessing import Manager, Process


# 进程是并行
def f(d, l, n):
    d[n] = '1'
    d["2"] = '2'
    l.append(n)

    print(d)
    print(l)
    print(n)
    print('子线程sub..')


if __name__ == '__main__':

    manager = Manager()  # 进程通信管理对象

    d = manager.dict()  # 创建进程通信字典{}
    l = manager.list(range(5))  # 创建进程通信列表[]

    p_list = []

    for i in range(5):
        p = Process(target=f, args=(d, l, i))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print(d)
    print(l)
    print('主线程manager..')