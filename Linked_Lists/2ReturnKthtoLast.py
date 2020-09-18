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
2.2 Return Kth to Last: implement an algorithm to find the kth to last element of a singly linked list
"""
"""
There could be various ways....we will solve it using two ways 
1-->recurssive
2-->non-recurssive
"""
"""
Recursive --> print the data
O(n) --> Space
O(n)  --> Time
"""


def kthtolastrec(temp, k):
    if temp.prev is None:
        return 0
    t = kthtolastrec(temp.prev, k) + 1
    if t == k:
        print(temp.data)
    return t


# llist = createfromlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# kthtolastrec(llist.givehead(), 1)

"""
A better solution is as follows.....we declare two pointers and place them "K" distances apart from each other an then travel till end
time --> O(n)
space --> O(1)
"""


def kthtolast(llist, k):
    temp = llist.givehead()
    frwd = temp
    back = temp
    p = -1
    while temp is not None:
        p += 1
        temp = temp.prev
        if p == k:
            break
    while temp is not None:
        back = back.prev
        temp = temp.prev
    print(back.data)


llist = createfromlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
kthtolast(llist, 0)
