class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(root):
    if root:
        print(root.data, end=", ")
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=", ")
        in_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=", ")

from collections import deque

def leve_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=", ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)