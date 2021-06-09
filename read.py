# f = open('C:/Users/19485/Desktop/read.txt', 'r')
# print(f.read())
# f.close()
# with open('C:/Users/19485/Desktop/read.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())
#         # print(line, end="")

with open('C:/Users/19485/Desktop/read.txt', 'r+') as t:
   for i in range(3):
       print(t.readline(), end="")