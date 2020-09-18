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
2.7 Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the j t h node of the second
linked list, then they are intersecting.
"""
"""
If both Lists end at same node...--> we have interection and then to find the  point we can travel both to 
the point of intersection
"""


def retinternsection(h1, h2):
    t1 = h1
    t2 = h2
    l1 = 0
    l2 = 0
    while t1.prev is not None:
        t1 = t1.prev
        l1 += 1
    while t2.prev is not None:
        l2 += 1
        t2 = t2.prev
    if t1 != t2:
        print("They do not intersect\n")
        return
    else:
        if l2 > l1:
            while l2 != l1:
                h2 = h2.prev
                l2 -= 1
        if l1 > l2:
            while l2 != l1:
                h1 = h1.prev
                l1 -= 1
        while h1 is not None:
            if h1 == h2:
                print("They Intersect at ==> " + str(h1) + "  Data --> " + str(h1.data))
                return
            h1 = h1.prev
            h2 = h2.prev


llist = createfromlist([3, 1, 5, 9])
llist2 = LList()
llist2.head = Node(4)
llist2.head.next = Node(6)
llist2.head.next.next = llist.head.prev.prev.prev #intersect at '9'

retinternsection(llist.head, llist2.head)
