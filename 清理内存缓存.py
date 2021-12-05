import subprocess


def clearMemCache(self):
    """
    清理 未及时回收的 内存缓存
    :return:
    """
    try:
        # sync: 将所有未写的系统缓冲区写到磁盘中，包含已修改的 i-node、已延迟的块 I/O 和读写映射文件
        # /proc/sys/vm/drop_caches: 写入不同数值，清理缓存的作用
        subprocess.getoutput(
            "sync;echo 1 > /proc/sys/vm/drop_caches;echo 2 > /proc/sys/vm/drop_caches;echo 3 > /proc/sys/vm/drop_caches")
    except Exception as e:
        print(e)