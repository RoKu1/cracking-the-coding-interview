from Trees_and_Graphs import Tree as tr

"""
4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent
Solution --> for each node the minimum of its right subtree is its inorder succesor but if Node does not have a right
subtree then --> it that parent which has a right subtree is its successor
"""
minel = -1  # considering all elements are positive


def minimumofsubtree(root):
    global minel
    if root is not None:
        minimumofsubtree(root.left)
        if root.data < minel or minel == -1:
            minel = root.data


def parentsrch(root):
    global minel
    while root is root.parent.right:
        root = root.parent
    minel = root.parent.data


def findsuccessor(node):
    if node.right is None:
        parentsrch(node)
    else:
        minimumofsubtree(node.right)
    print("The INORDER successor of this Node is --> " + str(minel))


tree = tr.arryaytotree([4, 5, 8, 9, 7, 1, 2, 3, 6])
findsuccessor(tree.root)  # for normal node
findsuccessor(tree.root.left.right.right)  # for rightmost node
findsuccessor(tree.root.right.right.left.left)