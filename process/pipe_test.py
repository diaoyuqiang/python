from multiprocessing import Process, Pipe


# 消费者为管道的一边
def consumer(p, name):
    while True:
        try:
            data = p.recv()
            print('%s拿到包子:%s' % (name, data))
        except Exception as e:
            p.close()
            break


# 生产者为管道的另一边
def producer(p, seq):
    for i in seq:
        p.send(i)
    else:
        p.close()


if __name__ == '__main__':
    parent_conn, sub_conn = Pipe()  # 创建双向管道

    # 创建子进程
    p = Process(target=consumer, args=(sub_conn, '顾客'))
    p.start()

    # 创建列表生成器
    seq = (x for x in range(10))
    producer(parent_conn, seq)

    parent_conn.close()
    sub_conn.close()

