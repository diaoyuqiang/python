from collections import deque
# q = deque()
# q.append() # 队尾进队
# q.popleft() # 队首出队
#
# # 双向队列
# q.appendleft() # 队首进队
# q.pop() # 队尾出队

def tail(n):
    with open('text.txt', 'r') as f:
        q = deque(f, n)
        return q

for line in tail(5):
    print(line, end="")

