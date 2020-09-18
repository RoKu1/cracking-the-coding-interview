class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def insert(self, data, root):
        if root is None:
            return Node(data)
        elif root.data >= data:
            root.left = self.insert(data, root.left)
            root.left.parent = root
            return root
        else:
            root.right = self.insert(data, root.right)
            root.right.parent = root
            return root

    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)


def arryaytotree(arry):
    mytree = Tree()
    for item in arry:
        mytree.root = mytree.insert(item, mytree.root)
    return mytree


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

# tree = arryaytotree([4, 5, 8, 9, 7, 1, 2, 3, 6])
# tree.inorder(tree.root)
