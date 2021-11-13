# except捕获异常处理
def temp_convert(var):
    try:
        return int(var)
    except ValueError:  # 捕获值错误异常
        print("参数中含有非数字")


num = temp_convert("x")
print(num)

# raise 抛出异常
def num(level):
    global a

    try:
        a = int(level)
        print(a)

    except Exception as e:
        a = 'None'
        return a


val = data = num('abc')
print(val)
    

# finally 无论如何都会执行的代码
try:
    fw = open(r"textfile.txt", "w", encoding="utf-8")

    try:
        fw.write("这是一个测试文件")
    finally:   # 异常与否都执行的代码
        print("关闭文件")
        fw.close()

except IOError:  # 捕获IO异常，并打印报错
    print("Error: 没有找到文件或读取文件失败")


# raise 抛出异常
def num(level):
    if level > 1:
        raise Exception
    else:
        return level


try:
    data = num(5)

except Exception as e:
    print("level过大")
else:
    print(data)
