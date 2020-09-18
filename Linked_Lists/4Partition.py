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
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If 'x' is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
Hints: #3, #24
"""
"""
Solution 1 ---> keep two pointers one at bigger element and one at smaller element --> this is oly when we copy 
the data...but to replace the node itself we will have to keep 4 pointers 
"""


def partion1(head, p):
    larg = head
    small = head
    flg = 0
    temp = head
    while temp is not None:
        if temp.data >= p:
            larg = temp
            flg = 1
        if temp.data < p and flg == 1:
            small = temp
        temp = temp.prev
    while small is not None:
        if small.data < p:
            t = larg.data
            larg.data = small.data
            small.data = t
            small = small.prev
        else:
            small = small.prev
            while larg is not None:
                if larg.data >= p:
                    break


# llist = createfromlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# partion1(llist.givehead(), 4)
# llist.printlist()

"""
Solution 2 ---> create two seprate lists and merge them 
"""


def partion2(temp, p):
    smllist = LList()
    smlend = smllist.head
    lrglist = LList()
    lrgend = lrglist.head
    while temp is not None:
        if temp.data < p:
            if smllist.head is None:
                smllist.head = temp
                smlend = smllist.head
            else:
                smlend.next = temp
                smlend = smlend.next
        if temp.data >= p:
            if lrglist.head is None:
                lrglist.head = temp
                lrgend = lrglist.head
            else:
                lrgend.next = temp
                lrgend = lrgend.next
        temp = temp.next
    lrgend.next = None
    smlend.next = lrglist.head
    smllist.printlist()


llist = createfromlist([3, 5, 8, 5, 10, 2, 1])
partion2(llist.givehead(), 5)
