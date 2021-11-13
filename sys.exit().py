import sys
import time

while True:
    res = input("Your favorite sports: ")
    if res.upper() == "EXIT":
        print("You've typed exit, and system will exit right now...")
        time.sleep(0.1)
        sys.exit()  # 程序直接退出，不捕捉异常
    print('You typed ' + res + '.')