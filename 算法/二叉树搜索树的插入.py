# 树的节点
import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

# 二叉搜索树
class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    # 递归插入的方法
    def insert(self, node, val):  # 当前节点以及要插入的值
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:  # 如果插入的值小于当前节点的值，插入到节点的左孩子位置
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:  # 如果插入的值大于当前节点的值，插入到节点的右孩子位置
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    # 非递归插入的方法
    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:  # 树非空，判断val跟p的值，如果val<p.data 插入左孩子，否，插入右孩子，相等直接返回
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    # 二叉树的查找 递归方式
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    # 二叉树的查找 非递归方式
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    # 二叉树的遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")


# tree = BST([4,6,7,9,2,1,3,5,8])
# tree.pre_order(tree.root)
# print("")
# tree.in_order(tree.root)
# print("")
# tree.post_order(tree.root)

li = list(range(0, 500, 2))
random.shuffle(li)
tree = BST(li)
print(tree.query_no_rec(3))