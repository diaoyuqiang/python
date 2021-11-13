class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.real = 0 # 队尾指针
        self.front = 0 # 队首指针

    def push(self, element): # 进队列
        if not self.is_filled():
            self.real = (self.real + 1) % self.size
            self.queue[self.real] = element
        else:
            raise IndexError("queue is filled")
    def pop(self): # 出队列
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("queue is empty")

    def is_empty(self):
        return self.real == self.front

    def is_filled(self):
        return (self.real + 1) % self.size == self.front


q = Queue(5)
for i in range(1, 5):
    q.push(i)
print(q.is_filled())
