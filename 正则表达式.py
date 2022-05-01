import re  # 正则模块 regular expression
"""
正则表达式：
1.字符相关  使用[],等价于 |, []可以匹配范围[0-9][a-z][A-Z] 使用[^aix]反向匹配除了aix之外的字符;
. 表示除换行符\n以外的任意字符, + 表示任意个数字符 ，? 阻断贪婪匹配
\\w代指字母或数字或下划线(汉字) \\d 数字 \\s 任意空白符

2.数量相关  * 重复0次或多次 + 重复至少1次 ？ 重复0次或者1次 {n} 重复n次 {n,} 重复至少n次 {n,m} 重复n-m次

3.() 括号分组, | 或匹配 
"""

text= "dsf130429191912015219k13042919591219521XkkT"  # 正则表达式提取身份证号码
# finditer实现正则分组命名 (?P<名称>正则)
data = re.finditer("\\d{6}(?P<year>\\d{4})(?P<month>\\d{2})(?P<day>\\d{2})\\d{3}[\\dXx]", text)  # finditer 返回迭代器类型
for i in data:
    info_dict = i.groupdict()  # 分组转换成字典
    print(info_dict)

# findall 立即返回提取的所有数据
data1 = re.findall("(\\d{6}(?P<year>\\d{4})(?P<month>\\d{2})(?P<day>\\d{2})\\d{3}[\\dXx])", text)
print(data1)

# match 方法从字符串开始匹配，返回第一个对象，未匹配到返回None
text = "大小逗2B最逗3B欢乐"
data2 = re.match("\\dB", text)
print(data2)  # 返回None，只能从起始位置进行匹配判断

# match匹配到的值用group()方法输出
text = "逗2B最逗3B欢乐"
data3 = re.match("逗\\dB", text)
print(data3.group())

print("*" * 20)
txt = "friday:186"
r = re.match("friday:(.*)(\\d)", txt)  # ():进行分组,match匹配不到返回None
if r is None:
    print("NOT")
else:
    print(r.group(1))

# sub 方法替换匹配成功的位置
text = "逗2B最逗3B欢乐"
data4 = re.sub("逗\\dB", "沙雕", text)
print(data4)

# split 方法根据匹配成功的位置进行分割 参数1表示只分割第一个匹配的位置
text = "逗2B最逗3B欢乐"
data5 = re.split("逗\\dB", text, 1)
print(data5)

# l = []
# if not l:
#     print("l")

# 数据格式校验 开始位置 ^ 结束位置 $
text1 = input("请输入邮箱：")
email_list = re.findall("^\\w+@\\w+.\\w+$", text1, re.ASCII)
if not email_list:
    print("邮箱格式错误")
else:
    print("你的邮箱是： %s" % email_list)