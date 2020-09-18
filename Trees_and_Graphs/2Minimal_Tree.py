from Trees_and_Graphs import Tree as tr
import math

"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
"""
"""
We can use a AVL tree for this but we will solve it using Binary search algorithm
"""
tree = tr.Tree()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def minimaltree(start, end):
    global arr
    if start < end:
        return
    mid = (start + end) // 2
    if start == end:
        tree.insert(mid, tree.root)
        return
    tree.insert(mid, tree.root)
    minimaltree(start, mid - 1)
    minimaltree(mid + 1, end)


height = math.floor(math.log2(len(arr))) + 1
tree.inorder(tree.root)
print("\nHeight is --> " + str(height))
