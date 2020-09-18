class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LList:
    def __init__(self):
        self.head = None

    def givehead(self):
        return self.head

    def printlist(self):
        temp = self.head
        while temp is not None:
            if temp.next is not None:
                print(temp.data, end=" -->")
            else:
                print(temp.data)
            temp = temp.prev


def createfromlist(Arr):
    llist = LList()
    last = None
    for each in Arr:
        if llist.head is None:
            llist.head = Node(each)
            last = llist.head
        else:
            last.next = Node(each)
            last = last.next
    return llist


"""
2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list
"""
"""
Solution ---> to just detect the loop...we need two pointers and O(n)..
But to detect where this starts we would need a HashMap --> traverse and go on adding the addresses to 
Map...moment it repeats we have the Pount of intersection
"""


def loopdetect(h1):
    Lmap = dict()
    while h1 is not None:
        if Lmap.get(h1):
            print("There is a loop at %   and Data --> %d " % (h1, h1.data))
            return
        Lmap[h1] = 1
        h1 = h1.prev
    print("No Loop ;) \n")


llist = createfromlist([1, 2, 3, 4, 5])
# llist.head.next.next.next.next.next = llist.head.next.next
loopdetect(llist.head)
