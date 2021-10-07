import calendar  # 年份日历模块

# 打印2021年的日历 w:天数之间的宽度，默认2  l:一周显示几行  c:并排两个月之间的宽度,默认6 m:并排显示月份个数，默认3
print(calendar.calendar(2021, w=2, l=1, c=6, m=6))

# 判断是否是闰年
print(calendar.isleap(2016))  # True
print(calendar.isleap(2019))  # False