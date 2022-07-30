# import traceback  # 用于提取，格式和打印Python程序的堆栈痕迹
# try:
#     1/0
# except Exception as e:
#     # print(e)
#     traceback.print_exc()  # 输出详细的异常信息到控制台

from io import StringIO
import traceback

a = ["hello", "yoyo"]

fp = StringIO()  # string io
try:
    print(a[4])
except Exception as e:
    traceback.print_exc(file=fp)

print("----后续代码用到地方读出来----")
print(fp.getvalue())
