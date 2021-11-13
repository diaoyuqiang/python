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

    def in_order(self, root):  # 中序遍历满足升序
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    # 删除数节点的情况分类
    # 情况1 node为叶子节点
    def __remove_node_1(self, node):
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # 如果为父节点的左孩子
            node.parent.lchild = None
        else:  # 如果为父节点的右孩子
            node.parent.rchild = None

    # 情况2.1 node只有一个左孩子
    def __remove_node_21(self, node):
        if not node.parent:  # node为根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node 为父节点的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # node为父节点的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # 情况2.2 node只有一个右孩子
    def __remove_node_22(self, node):
        if not node.parent:   # node为根节点
            self.root = node.rchild
        elif node == node.parent.lchild:  # node 为父节点的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:  # node 为父节点的左孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    # 删除树节点
    def delete(self, val):
        if self.root:  # 判断树不为空
            node = self.query_no_rec(val)
            if not node:  # 如果节点不存在，返回false
                return False
            if not node.lchild and not node.rchild:  # node为叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # node只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # node只有一个右孩子
                self.__remove_node_22(node)
            else:  # node有两个孩子节点
                min_node = node.rchild
                while min_node.lchild:  # 查找右子树中最小的节点
                    min_node = min_node.lchild
                node.data = min_node.data  # min_node替换node的数据
                # 删除min_node
                if min_node.rchild:  # 如果min_node有右孩子
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)




