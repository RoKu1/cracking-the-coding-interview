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
2.7 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""


def removedupes1(llist):
    prevtemp = llist.givehead()
    temp = prevtemp.prev
    hashmap = dict()
    hashmap[prevtemp.data] = 1
    while temp is not None:
        """
        handle where  there is only one node 
        """
        if hashmap.get(temp.data):
            prevtemp.prev = temp.prev
            temp = temp.prev

        else:
            hashmap[temp.data] = 1
            prevtemp = temp
            temp = temp.prev
    return llist


"""
Solution is 
O(n) --> Time
O(n) --> Space
just traverse the list and go on adding the elements to HashMap --> thus when we get a double delete and join  
"""
llist = createfromlist([1])
llist = removedupes1(llist)
llist.printlist()

"""
Solution is 
O(n*n) --> Time
O(1) --> Space
just traverse the list with two pointers like two for loops  
"""


def removedupes2(llist):
    temp1 = llist.givehead()
    while temp1 is not None:
        temp2 = temp1
        while temp2.prev is not None:
            if temp2.prev.data == temp1.data:
                temp2.prev = temp2.prev.prev
            else:
                temp2 = temp2.prev
        temp1 = temp1.prev
    return llist


llist2 = createfromlist([1, 1, 2, 3, 4, 5, 6, 7, 6, 0, 1])
llist2 = removedupes2(llist2)
llist2.printlist()
