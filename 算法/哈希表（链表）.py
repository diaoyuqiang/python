class LinkList:
    class Node:  # 创建节点（域、指针）
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:  # 创建链表迭代器
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item  # 返回当前节点的数据域
            else:
                raise StopIteration  # 节点为空时停止迭代

        def __iter__(self):  # 返回链表
            return self

    def __init__(self, iterable=None): # 传入列表数据
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s  # 链表尾插法

    def extend(self, iterable):
        for obj in iterable:  # 遍历链表中的数据进行插入
            self.append(obj)

    def find(self, obj):  # 查找链表中的值，找到返回True，否 False
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)  # 返回链表迭代器，LinkList为可迭代对象

    def __repr__(self):
        return "<<"+",".join(map(str, self))+">>"  # 返回可迭代对象（self类似于集合的结构）的字符串形式，map函数进行序列的映射


class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]  # 创建空的寻址表（寻址表每个位置对应一个链表）

    def h(self, k):  # 定义哈希函数
        return k % self.size

    def insert(self, k):  # 插入k值
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert.")
        else:
            self.T[i].append(k)

    def find(self, k):  # 查找k值是否存在
        i = self.h(k)
        return self.T[i].find(k)


ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
print(','.join(map(str, ht.T)))
# print(",".join(map(str, ht.T)))
# print(ht.find(202))
