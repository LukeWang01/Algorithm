class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("root/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return

        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        else:
            raise ValueError("No path")


tree = FileSystemTree()
tree.mkdir("luke")
tree.mkdir("bin/")
tree.mkdir("var/")
tree.cd("var/")
tree.mkdir("tmp/")
print(tree.ls())
tree.cd("../")
print(tree.ls())
print(tree.root.children)