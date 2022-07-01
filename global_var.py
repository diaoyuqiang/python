message = "唯有被追赶的时候，你才能真正地奔跑"  # 全局变量
print("全局变量message =", message, id(message))  # 在函数体外调用全局变量

# 在函数体内修改全局变量的值
def f_demo():
    global message  # global关键字, 将message声明为全局变量(message标签被分配给了新的内存地址)
    message = "命运给予我们的不是失望的酒，而是机会之杯"  # 全局变量值
    print("全局变量message =", message, id(message))  # 在函数体内调用全局变量
f_demo()  # 调用函数
print("全局变量message =", message, id(message))  # 在函数体外调用全局变量

# num = 1
# print(num, id(num))
#
# def run(num):
#     num = 2  # 函数内部作用域的变量
#     print(num, id(num))
#     return num
#
# num = run(num)
# print("end", num, id(num))