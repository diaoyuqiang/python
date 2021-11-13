from blance_tree import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0   # blance_factor 平衡因子


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):  # 自平衡二叉搜索树左旋
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):  # 自平衡二叉搜索树右旋
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):  # 自平衡二叉搜索树右旋、左旋
        g = c.lchild
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parnet = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # g为插入节点，bf都为0
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):  # 自平衡二叉搜索树左旋、右旋
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:  # g为插入节点，bf都为0
            p.bf = 0
            c.bf = 0
        return g

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = AVLNode(val)
            return
        while True:  # 树非空，判断val跟p的值，如果val<p.data 插入左孩子，否，插入右孩子，相等直接返回
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # node为插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:
                return
        # 更新bf因子
        while node.parent:  # node.parent不空
            if node.parent.lchild == node:  # 传递是从左子树来的，左子树更沉
                # 更新bf -= 1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1, 更新后变成-2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 连接旋转后的子树
                    x = node.parent
                    if node.bf > 0:  # 旋转前子树的根
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)

                    # n 和 g最后要连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1, 更新之后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0, 更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 传递是从右子树来的，右子树更沉了
                # 更新node.parent.bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf == 1, 更新之后变成2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 用于连接旋转后的树
                    x = node.parent  # 记录旋转之前子树的根
                    if node.bf < 0:  # node.bf = 1
                        n = self.rotate_right_left(node.parent, node)
                    else:  # node.bf = -1
                        n = self.rotate_left(node.parent, node)
                        # 记得连起来
                elif node.parent.bf < 0:  # 原来node.parent.bf = -1,更新之后变成0
                    node.parent.bf = 0
                    break
                else:  # node.parent.bf = 0, 更新之后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 链接旋转后的子树
            n.parent = g
            if g:  # g不为空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)






