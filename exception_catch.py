import time

def run(n):
    if n < 3:
        print("n<3")
    else:
        raise SystemExit()  # 退出解释器

    print("eeeeee")

# run(5)

while True:
    try:
        print("1111")
        time.sleep(2)
    except KeyboardInterrupt as e:  # 程序终端异常
        print("ctrl + c")
        break