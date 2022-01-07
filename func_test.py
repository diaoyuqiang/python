import random

def run(n):
    if n > 0:
        print("ok")
        return True

def sum():
    a = random.randint(1, 5)
    print(a)

    if not run(a):
        print("next")

sum()