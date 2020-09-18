from Trees_and_Graphs import Tree as tr

"""
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
Hints: #21, #33, #49, #105, #124
"""

"""
For Solution of this problem we have written a function to find height of tree given root
now we just need to use this function reccurssively 
"""

tree = tr.arryaytotree([4, 5, 8, 9, 7, 1, 2, 3, 6])
tree2 = tr.arryaytotree([10, 5, 15, 2, 8, 12, 18, 1, 3, 6, 9, 11, 13, 16, 19])


def checkbal(root):
    if root is None:
        return True
    if abs(tr.height(root.left) - tr.height(root.right)) > 1:
        return False
    else:
        return checkbal(root.left) and checkbal(root.right)


if checkbal(tree2.root):
    print("It is balanced\n")
else:
    print("It is not balanced\n")

