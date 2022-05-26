import os

def bak_using_file(file_path):
    """
    备份正在使用的文件
    """
    bak_path_file = file_path + ".bak"
    if os.path.exists(bak_path_file):
        # 删除之前备份的路径点图
        delete_old_path_command = "rm -f {}".format(bak_path_file)
        # "".split()  # 默认以空格分割
        # ret = os.popen(shell)  # 接受输出内容
        os.system(delete_old_path_command)  # 执行系统命令 (不接受返回内容，只有0(成功)1,2 是否成功的信号代码)
    bak_path_command = "mv " + file_path + " " + bak_path_file
    os.system(bak_path_command)