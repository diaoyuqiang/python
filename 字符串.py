# 构建字符串 字符集：ASCII unicode gbk gbk2312 utf-8
""""
字符串是一种容器，且不可变

"""
# 不换行续写
msg = "来自十年\
后的你。"
data = "来自十年后的你"\
    "新世界。"

# 换行
msg1 = """
来自十年后的你
新世界
"""
print(msg)
print(data)
print(msg1)

# 转义符 \ + 字母或者符号  -- \r 回车 \t 横向制表符 \n 换行  \a 响铃 \b 退格
str_ = 'I\'M xiaoming'
str_1 = r"c:\now"  # 字符串前加r保留原有格式
print(str_)
print(str_1)
print("\a")
print("北京大学\r西北")  # 覆盖本行
print("清华大学\r\n东南")  # 回车换行

# 拼接查询语句
name, age = "xiao", 18
msg = "select * from student where name='"+name+"'and age="+str(age)
msg1 = "select * from student where name='%s' and age=%d" % (name, age)
msg2 = "select * from student where name=%r and age=%d" % (name, age)  # %r 原始字符串
print(msg)
print(msg1)
print(msg2)

# 字符串分片（左闭右开）
str_2 = "心之所动切就随风而去"
print(str_2[1:3])  # 输出索引位置1~2
print(str_2[:])
print(str_2[-2:])

# 字符串格式化
print("银行余额 %g" % 123.12345)  # 浮点数取整，如果有小数部分保留三位，如果有0按0截取
print("银行余额 %5g" % 123.02045)  # 有0按0截取

# format()
print("有引号 {!r}, 没有引号 {!s}".format("text1", "test2"))
print("{}, {}".format("liu", "20"))  # 可以不指定索引
print("{0},{1},{0}".format("test", 18))  # 可以复用索引
print("{name}, {age}".format(name="小明", age=18))  # 键值对方式
# < 左对齐  > 右对齐  ^ 居中
print("{:<8}".format(211))  # 默认空格填充，返回8位，左对齐
print("{:#<8}".format(211))  # 指定填充字符
print("{:,.2f}".format(12345.5678))  # 千分位取整，保留2位小数
print("{0[0]}, {0[1]}".format(["小白", 18]))  # 访问列表元素
print("int: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:08b}".format(27))  # 转换进制

# f字符串格式化
name = "Tom"
age = 3
print(f"His name is {name}, he's {age} years old.")  # {}相当于变量引用


# 访问类属性
class Book:
    def __init__(self, nm, pc):
        self.name, self.price = nm, pc

    def __str__(self):  # 返回一个对象的描述信息
        return "书名是：{s.name}, 价格是：{s.price}".format(s=self)


print(str(Book("小说", 15)))


class Cat:
    """定义一个猫类"""

    def __init__(self, new_name, new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        # self.name = "汤姆"
        # self.age = 20
        self.name = new_name
        self.age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
        num = 100  # num是一个局部变量,当这个函数执行完之后,这个变量的内存空间就没有了,因此其他方法不能使用这个变量
        print(num)

    def __str__(self):
        """返回一个对象的描述信息"""

        return "名字是:%s , 年龄是:%d" % (self.name, self.age)

    def eat(self):
        print("%s在吃鱼...." % self.name)

    def drink(self):
        print("%s在喝可乐..." % self.name)

    def introduce(self):
        # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
        # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))


# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom)