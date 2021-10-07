# import threading
#
#
# def playMusic():
#     print("此处播放音乐")
#
#
# time = threading.Timer(5, playMusic)
# time.start()


lst = ['202102003', '202101001', '2021011002', '2021021004', '2021031005']

result = sorted(lst, key=lambda x: x[4:6])  # 指定可迭代对象中的一个元素来进行排序， 参数为可迭代对象中的一个元素[4: 6]（左闭右开）
print(result)

print(lst[1])