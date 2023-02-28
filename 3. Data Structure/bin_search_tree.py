class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self, lst=None):
        self.root = None
        if lst:
            for i in lst:
                self.insert_no_recursion(i)

    def __remove_node_1__(self, node):
        # 1. node has no child
        if not node.parent:
            # only have root node
            self.root = None
        if node == node.parent.left:
            node.parent.left = None
            # node.parent = None this line can be removed
        else:
            node.parent.right = None

    def __remove_node_2__(self, node):
        # 2. node only has one child
        if node.left:
            # 2.1 only has left child
            if not node.parent:
                self.root = node.left
                node.left.parent = self.root
            elif node == node.parent.left:
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        if node.right:
            # 2.2 only has right child
            if not node.parent:
                self.root = node.right
                node.right.parent = self.root
            elif node == node.parent.left:
                node.parent.left = node.right
                node.right.parent = node.parent
            else:
                node.parent.right = node.right
                node.right.parent = node.parent

    def delete_node(self, val):
        if self.root:
            node = self.query_no_recursion(val)
            if node:
                if not node.left and not node.right:
                    # has no child
                    self.__remove_node_1__(node)
                elif not node.right:
                    # only has left
                    self.__remove_node_2__(node)
                elif not node.left:
                    # only has right
                    self.__remove_node_2__(node)
                else:
                    # has two children
                    min_node = node.right  # search from the right and find the min node
                    while min_node.left:
                        min_node = node.left
                    node.data = min_node.data
                    if min_node.right or min_node.left:
                        self.__remove_node_2__(min_node)
                    else:
                        self.__remove_node_1__(min_node)
            else:
                print("node not found")
        else:
            print("tree is empty")

    def query(self, node, val):
        if not node:
            return None
        if val < node.data:
            return self.query(node.left, val)
        elif val > node.data:
            return self.query(node.right, val)
        elif val == node.data:
            return node

    def query_no_recursion(self, val):
        p = self.root
        while p:
            if val < p.data:
                p = p.left
            elif val > p.data:
                p = p.right
            else:
                return p
        return None

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        if val < node.data:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.data:
            node.right = self.insert(node.right, val)
            node.right.parent = node

        return node

    def insert_no_recursion(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = BiTreeNode(val)
                    p.left.parent = p
                    return
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BiTreeNode(val)
                    p.right.parent = p
                    return
            else:
                return

    def pre_order(self, root):
        if root:
            print(root.data, end=", ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=", ")
            self.in_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=", ")


import random

# lst = [i for i in range(500)]
# random.shuffle(lst)
#
# tree = BST(lst)
# tree.pre_order(tree.root)
# print("")
# tree.in_order(tree.root)  # printed in order
# print("")
# tree.post_order(tree.root)
# print("")
# print(tree.query(tree.root, 4).data)
# print(tree.query_no_recursion(4).data)

# tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
# tree.in_order(tree.root)
# print("")
# tree.delete_node(4)
# tree.delete_node(4)
# tree.delete_node(8)
# tree.in_order(tree.root)
