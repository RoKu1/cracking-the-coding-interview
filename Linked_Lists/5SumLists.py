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
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: ( 7 - > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295,
Output:9 -> 1 -> 2,Thatis,912.
Hints: #7, #30, #71 #95, #109
"""

"""
Solution --> for Reverse order 
It is easy -> as we know that we can start adding from the head__
TimeComplx --> O(max(n,m)) --> n and m being the length

"""


def sumlist(head1, head2):
    carry = 0
    sumlst = LList()
    sumend = sumlst.head
    while head1 is not None and head2 is not None:
        s = head1.data + head2.data + carry
        if s == 10:
            carry = 1
        else:
            carry = s // 10
        if sumlst.head is None:
            sumlst.head = Node(s % 10)
            sumend = sumlst.head
        else:
            sumend.next = Node(s % 10)
            sumend = sumend.next
        head1 = head1.next
        head2 = head2.next
    while head1 is not None:
        s = head1.data + carry
        if s == 10:
            carry = 1
        else:
            carry = s // 10
        sumend.next = Node(s % 10)
        head1 = head1.next
    while head2 is not None:
        s = head2.data + carry
        if s == 10:
            carry = 1
        else:
            carry = s // 10
        sumend.next = Node(s % 10)
        head2 = head2.next
    if carry:
        sumend.next = Node(1)
    return sumlst


sumlst = sumlist(createfromlist([7, 1, 6, 3]).head, createfromlist([5, 9, 3, 6]).head)
# sumlst.printlist()

"""
Solution for forward order ==>
  Just reverse bot linked list -->  max O(n)+O(m) for that and O(n) of above
  2O(n)+O(m) --> O(n)   
"""


def revlist(llist):
    prev = None
    curr = llist.head
    nxt = curr.next
    while nxt is not None:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next
    curr.next = prev
    llist.head = curr
    return llist


l1r = revlist(createfromlist([3, 6, 1, 7]))
l2r = revlist(createfromlist([6, 3, 9, 5]))
sumlst = revlist(sumlist(l1r.head, l2r.head))
# sumlst.printlist()


"""
Doing the forward one with recurssive function
1--> first we need to pad the shorter list with zeros
2--> do the rest
"""

sumlst2 = LList()


def length(temp):
    l = 0
    while temp is not None:
        l += 1
        temp = temp.prev
    return l


def sumlist2(llist1, llist2):
    l1 = length(llist1.head)
    l2 = length(llist2.head)
    # We equalize the lengths by padding zeros at start of lists
    if l1 != l2:
        if l1 < l2:
            missingnodes = l2 - l1
            for i in range(0, missingnodes):
                node = Node(0)
                node.next = llist1.head
                llist1.head = node
        else:
            missingnodes = l1 - l2
            for i in range(0, missingnodes):
                node = Node(0)
                node.next = llist2.head
                llist2.head = node
    llist1.printlist()
    llist2.printlist()
    carry, sumhead = recuaddition(llist1.head, llist2.head)
    print(carry)
    if carry:
        node = Node(1)
        node.next = sumhead
        sumlst2.head = node
    sumlst2.printlist()


def recuaddition(h1, h2):
    if h1.prev is None and h2.prev is None:
        if h1.data + h2.data == 10:
            carry = 1
        else:
            carry = (h1.data + h2.data + 0) // 10
        s = (h1.data + h2.data + 0) % 10
        sumlst2.head = Node(s)
        print("Node -> " + str(s) + "Carry is --> " + str(carry))
        return carry, sumlst2.head
    carry, temp = recuaddition(h1.prev, h2.prev)
    s = (h1.data + h2.data + carry) % 10
    if (h1.data + h2.data + carry) == 10:
        carry = 1
    else:
        carry = (h1.data + h2.data + carry) // 10
    node = Node(s)
    node.next = temp
    sumlst2.head = node
    print("Node -> " + str(s) + "Carry is --> " + str(carry))
    return carry, sumlst2.head


sumlist2(createfromlist([9, 9, 9, 9]), createfromlist([9, 9, 9]))
