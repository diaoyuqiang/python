from socket import *
import subprocess  # 与系统交互的模块

ip_port = ("127.0.0.1", 5030)
back_log = 5
buf_size = 1024

# 创建socket连接
cmd_server = socket(AF_INET, SOCK_DGRAM)
cmd_server.bind(ip_port)

while True:
    # 防止客户端中断，导致程序报错
    try:
        cmd, add = cmd_server.recvfrom(buf_size)  # 接收客户端的数据
        if not cmd:
            break  # 如果客户端发送空，中断本次通信
        print("客户端的指令为：", cmd.decode())
        # 执行指令
        """
        关键字参数 | 位置参数
        arg 指令序列或指令字符串
        shell=False True为字符串 False为字节序列
        stderr=None(返回错误通道信息) subprocess.PIPE 返回一个file，可以直接给客户端展示
        stdin=None(标准输入)
        stdout=None(标准输出)
        """

        # 执行指定
        cmb_result = subprocess.Popen(cmd.decode("utf-8"), shell=True,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
        """
        cmd 发送命令后，可能会返回两种结果：
        1.错误指令 返回错误通道信息
        2.正确指令 返回标准输出:
            a.执行成功返回空，进行友好提示
            B.执行成功 返回标准输出信息       
        """
        err_msg = cmb_result.stderr.read()  # 从错误通道获取信息
        if err_msg:  # 如果错误通道有数据，返回错误信息
            msg = err_msg  # 从错误通道获取信息
        else:  # 如果错误通道没数据，返回标准输出
            msg = cmb_result.stdout.read()  # 从标准输出获取信息

    # 执行cd. cd.. 这种命令时返回为空的处理
        if not msg:
            conn.send("执行成功".encode("gbk"))  # 返回客户端友好提示
            continue

        cmd_server.sendto(msg, add)

    except Exception as e:
        print("程序异常，异常信息为：", e)
        break
# 与客户端断开连接
cmd_server.close()





