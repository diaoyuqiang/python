# 不支持 OS_REUSEPORT 未完成模块
# import sys
# import socket
# import multiprocessing
# import contextlib
# import json
# from concurrent import futures
# import time
# import grpc
# import hello_bilbil_pb2
# import hello_bilbil_pb2_grpc
# import datetime
#
# _PROCESS_COUNT = multiprocessing.cpu_count()  # 获取cpc内核数
# _THREAD_CONCURRENCY = _PROCESS_COUNT  # 线程数等于当前进程数
# _ONE_DAY = datetime.timedelta(days=1)
#
#
# @contextlib.contextmanager
# def _reserve_port():
#    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)  # 实例化socket
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
#
#    if sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 0:  # SO_REUSEPORT 多进程功能
#        raise RuntimeError("Failed to set SO_REUSEPORT.")
#    sock.bind("", 50052)  # 绑定端口号
#    try:
#        yield sock.getsockname()[1]  # 返回端口号
#    finally:
#        sock.close()  # 关闭socket
#
# def main():
#     with _reserve_port() as port:
#         sys.stdout.flush()  # 刷新缓存
#         workers = []  # 要启用的进程列表
#
#         for _ in range(_PROCESS_COUNT):
#             worker = multiprocessing.Process(target=serve, args=(port, ))
#             worker.start()
#             workers.append(worker)
#
#         for worker in workers:
#             worker.join()
#
#
# if __name__ == "__main__":
#     main()
