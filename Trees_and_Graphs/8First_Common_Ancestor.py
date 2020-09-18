from Trees_and_Graphs import Tree

"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""
"""
Solution --> what we need to do is implement a searh function that will return the node that it finds...
That is we if it finds none of given nodes --> returns Null
If one of them is found --> returns the found node
If both are found --> 
"""
tree = Tree.arryaytotree([4, 5, 8, 9, 7, 1, 2, 3, 6])
node1 = 9
node2 = 6


def FCA(root):
    global node1, node2
    if root is None:
        return None
    if root.data == node1 or root.data == node2:
        return root

    left = FCA(root.left)
    right = FCA(root.right)

    if left is not None and right is not None:
        return root

    else:
        if left is None:
            return right
        else:
            return left


ancestor = FCA(tree.root)
print(ancestor.data)
