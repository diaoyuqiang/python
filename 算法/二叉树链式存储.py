from collections import deque


# 二叉树的链式存储节点
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e  # e为根节点

# 二叉树的遍历 4种方法


# 1.二叉树的前序遍历
def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


# 2.二叉树的中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


# 3.二叉树的后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


# 4.二叉树的层次遍历
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()  # node接收出队的元素
        print(node.data, end=",")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


level_order(root)
