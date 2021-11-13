import os
import glob  # 文件名模式匹配
import time


def rem(num):

    # 根据文件创建时间排序，删除较早的文件
    lis = sorted(glob.glob(r'D:\python_job\*'),
                 key=lambda x: time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(x))),
                 reverse=True)

    for file in lis[num:]:
        os.remove(file)

