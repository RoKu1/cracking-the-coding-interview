"""
3.3
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure Set Of Stacks that mimics this. Set Of Stacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
Set Of Stacks. push( ) and S e t O f S t a c k s . p o p ( ) should behave identically to a single stack
(that is, p o p ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function p o p A t ( i n t i n d e x ) which performsa pop operation on a specific sub-stack.
"""


class Substack:
    def __init__(self):
        self.items = []
        self.prev = None

    def pushsubstack(self, data):
        self.items.append(data)

    def popsubstck(self):
        return self.items.pop(-1)

    def isfull(self):
        return len(self.items) == 10

    def printstck(self):
        print(self.items, end="\n")

    def isempty(self):
        return self.items == []


class StackofPlates:
    def __init__(self):
        self.head = None
        self.lenth = 0

    def push(self, data):
        if self.head is None:
            self.head = Substack()
            self.head.pushsubstack(data)
            self.lenth += 1
            return
        else:
            if self.head.isfull():
                temp = Substack()
                temp.pushsubstack(data)
                temp.prev = self.head
                self.head = temp
                self.lenth += 1
            else:
                self.head.pushsubstack(data)

    def pop(self):
        if self.head.isempty():
            self.lenth -= 1
            self.head = self.head.prev
        return self.head.popsubstck()

    def popatindex(self, index):
        index = self.lenth - index - 1
        temp = self.head
        while index:
            temp = temp.prev
            index -= 1
        else:
            ret = temp.popsubstck()
            self.refrshstcks()
            return ret

    def refrshstcks(self):
        if self.head.prev is None:
            return
        temp = self.head
        t2 = temp.prev
        print("In rfrsg")
        while t2.prev is not None:
            if t2.isempty():
                temp.prev = t2.prev
                t2 = t2.prev

            else:
                t2 = t2.prev
                temp = temp.prev

    def printallstacks(self):
        temp = self.head
        while temp is not None:
            temp.printstck()
            temp = temp.prev


def createfrom(stck):
    for i in range(1, 100):
        stck.push(i)
    return stck


# def refrshstcks(head):
#     if head.prev is None:
#         return
#     temp = head
#     t2 = temp.prev
#     print("In rfrsg")
#     while t2.prev is not None:
#         if t2.isempty():
#             temp.prev = t2.prev
#             t2 = t2.prev
#         else:
#             t2 = t2.prev
#             temp = temp.prev


stck = StackofPlates()
stck = createfrom(stck)
stck.printallstacks()
stck.pop()
stck.printallstacks()
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.popatindex(1)
stck.printallstacks()
print(stck.lenth)
