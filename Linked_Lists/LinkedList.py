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
            temp = temp.next


def insertintolist(data, llist):
    if llist.head is None:
        llist.head = Node(data)
    else:
        temp = llist.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)


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
