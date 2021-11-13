"""
输入一个十六进制的数值字符串。注意：一个用例会同时有多组输入数据。
"""
while True:
    try:

        a = input()
        b = int(a, 16)
        print(b)
    except (EOFError, KeyboardInterrupt):
        break