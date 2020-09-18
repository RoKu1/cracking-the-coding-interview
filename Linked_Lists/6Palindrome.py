"""
Palindrome: Implement a function to check if a linked list is a palindrome,
"""


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
There are many solutions --> reverse the linkedlist and copy or save the reverse in array/stack(stack makes the linear
travesal reverse) or write recuursive function to save reverse -->

Solution --> linear reverse travel and save in a array and check in a the reverse
 --> To linear reverse travel --> recurrsive function or save data in stack
Time --> 2O(n)
"""
llist = createfromlist([1, 2, 3, 4, 5, 6, 5, 4, 3, 2])


def checkpalindrome(head):
    revlist.append(recsaverev(llist.head))
    for el in revlist:
        if el != head.data:
            print("Not a Palindrome")
            return
        head = head.next
    print("A palindrome")


revlist = []


def recsaverev(head):
    if head.prev is None:
        return head.data
    revlist.append(recsaverev(head.prev))
    return head.data


checkpalindrome(llist.head)
