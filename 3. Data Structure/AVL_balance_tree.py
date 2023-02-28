from bin_search_tree import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # balance factor


class AVLTree(BST):
    def __init__(self, lst):
        BST.__init__(self, lst)

    def rotate_left(self, p, c):
        s2 = c.left
        p.right = s2
        if s2:
            s2.parent = p
        c.left = p
        p.parent = c

        # update balance factor
        p.bf = 0
        c.bf = 0

        return c

    def rotate_right(self, p, c):
        s2 = c.right
        p.left = s2
        if s2:
            s2.parent = p
        c.right = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right_left(self, p, c):
        g = c.left
        s2 = g.left
        s3 = g.right
        p.right = s2
        if s2:
            s2.parent = p
        c.left = s3
        if s3:
            s3.parent = c
        g.left = p
        g.right = c
        p.parent = g
        c.parent = g

        if g.bf > 0:  # right side height is greater
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # all children are empty
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.right
        s2 = g.left
        s3 = g.right
        c.right = s2
        if s2:
            s2.parent = c
        p.left = s3
        if s3:
            s3.parent = p
        g.left = c
        g.right = p
        c.parent = g
        p.parent = g

        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else:
            p.bf = 0
            c.bf = 0
        return g

    def insert_no_recursion(self, val):
        # find the node
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = AVLNode(val)
                    p.left.parent = p
                    node = p.left  # inserted node
                    break
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = AVLNode(val)
                    p.right.parent = p
                    node = p.right  # inserted node
                    break

            else:  # val == p,
                return

        # 2. update balance factor
        while node.parent:  # node parent is not empty
            if node == node.parent.left:
                # inserted from left
                if node.parent.bf < 0:  # -1 - 1 = -2; only can be -1, 0, 1 in the beginning
                    g = node.parent.parent
                    x = node.parent  # subtree root before rotate
                    if node.bf > 0:  # insert right,
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # g.left = n    # connect
                    # n.parent = g

                # inserted from right
                elif node.parent.bf > 0:  # 1 - 1 = 0; only can be -1, 0, 1 in the beginning
                    node.parent.bf = 0  # no need to rotate
                    break

                else:  # 0 - 1 = -1; only can be -1, 0, 1 in the beginning
                    node.parent.bf = -1
                    node = node.parent
                    continue

            else:
                # inserted from right
                if node.parent.bf < 0:  # -1 + 1 = 0; only can be -1, 0, 1 in the beginning
                    node.parent.bf = 0
                    break

                elif node.parent.bf > 0:  # 1 + 1 = 0; only can be -1, 0, 1 in the beginning
                    g = node.parent.parent
                    x = node.parent  # subtree root before rotate
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                    # n.parent = g    # connect
                    # g.right = n

                else:  # 0 + 1 = 1; only can be -1, 0, 1 in the beginning
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # connect
            n.parent = g
            if g:
                if x == g.left:
                    g.left = n
                else:
                    g.right = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9,8, 7, 6, 5, 4, 3, 2, 1])

tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
print()
tree.post_order(tree.root)

