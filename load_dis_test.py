import dis  # 将pycode转化成字节码

def demo():
    x=2
    x += 1

    if x < 3:
        return False
    else:
        return True

dis.dis(demo)  # 执行函数的栈信息
print(dis.code_info(demo))  # 打印函数详细信息