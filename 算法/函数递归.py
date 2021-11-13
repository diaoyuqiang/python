# 递归相加num
def sum_num(num):
    if num == 1: # 递归出口，否则会死循环
        return 1
    temp = sum_num(num - 1)
    return num + temp


result = sum_num(100)
print(result)

# 拆包 *args 元祖 *kwargs 字典
tuple1 = (1, 2, 3)
dict1 = {"name": "小明", "性别": "男"}


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(*tuple1, **dict1)

# 缺省参数
gl_num_list = [6, 3, 9]
gl_num_list.sort(reverse=True)
print(gl_num_list)


# 不可变和可变的参数
def demo(num, num_list):
    print("函数内部代码")
    # num = num + num
    num += num
    # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    num_list += num_list
    print(num)
    print(num_list)
    print("函数代码完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)