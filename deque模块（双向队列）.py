from collections import deque

# 双向队列
# q = deque() # 参数: 可迭代对象 | 队列长度

# q.append() # 队尾进队 | q.pop() # 队尾出队
# q.popleft() # 队首出队 | q.appendleft() # 队首进队


# deque读取日志
def tail(n):
    with open('text', 'r') as f:
        q = deque(f, n)
        # q.remove("llll")  # 删除队列中的元素
        return q

# 读取日志最后5行
for line in tail(5):
    print(line, end="")
