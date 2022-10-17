import os

# 路径拼接
"""
拼接规则: 从倒数第一个，以‘/’开头的参数开始拼接，之前的参数全部丢弃。
         以‘/’结尾的，以及参数中间有‘/’的，斜杠仅作为参数的一部分。
"""

a = os.path.join('\log', 'test.log')
# print(a)

def walkFile(file):
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        for f in files:
            print(os.path.join(root, f))
        # for d in dirs:
        #     print(os.path.join(root, d))

walkFile("D:\python_stu\protobuf_test")

def search_dir(path):
    files= os.listdir(path) # 得到文件夹下的所有文件名称
    # print(files)
    for file in files: # 遍历该文件夹
        fp = os.path.join(path, file)
        if os.path.isfile(fp):
            print(os.path.abspath(fp))

        elif os.path.isdir(fp):
            search_dir(fp)
        else:
            pass


# search_dir("D:\python_stu\protobuf_test")
