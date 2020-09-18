from Trees_and_Graphs import Tree as tr

"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
Solution --> just traverse this binary tree in inorder and if the list is sorted then we have a BST
"""
lst = []
tree = tr.arryaytotree([4, 5, 8, 9, 7, 1, 2, 3, 6])


def inordertraverse(root):
    global lst
    if root is None:
        return
    inordertraverse(root.left)
    lst.append(root.data)
    inordertraverse(root.right)


inordertraverse(tree.root)
print(lst)