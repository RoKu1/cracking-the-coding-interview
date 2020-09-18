from Trees_and_Graphs import Tree as tr
from Linked_Lists import LinkedList as LL

"""
4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
Hints: #107, #123, #135
"""
"""
We will implement a PreOrder traversal of Tree and then also pass level everytime so at each node we add it to 
List of particular level only
"""

tree = tr.arryaytotree([4, 5, 8, 9, 7, 1, 2, 3, 6])
collectionoflists = []


def listofdepths(root, level=0):
    global collectionoflists
    if root is not None:
        if level == len(collectionoflists):
            lst = LL.LList()
            LL.insertintolist(root.data, lst)
            collectionoflists.append(lst)
        else:
            LL.insertintolist(root.data, collectionoflists[level])
        listofdepths(root.left, level + 1)
        listofdepths(root.right, level + 1)


listofdepths(tree.root)
for list in collectionoflists:
    list.printlist()