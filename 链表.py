class Node: # 创建链表节点
    def __init__(self, item):
        self.item = item # 链表数据域
        self.next = None # 链表指针

# 链表头插法
def create_lklist_head(li):
    head = Node(li[0]) # 把列表第一个元素存入链表头部节点
    for element in li[1:]: # 遍历列表[1]往后的元素
        node = Node(element) # 存入链表的新节点里
        node.next = head  # 新节点指向原先头部节点
        head = node  # 新节点设置为头部节点
    return head

# 链表尾插法
def create_lklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_lklist(lk):
    while lk:
        print(lk.item, end=",")
        lk = lk.next

lk = create_lklist_tail([1,2,3,4])
print_lklist(lk)
