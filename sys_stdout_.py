import sys

temp = sys.stdout
f = open('text', "a+")
print("success")
sys.stdout = f
print("write")
sys.stdout = temp
print("common")
f.close()