"""
3.4
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop(-1)

    def printstck(self):
        for item in self.items:
            print(item, end="->")


class MyQueue:
    def __init__(self):
        self.oldstack = Stack()
        self.newstack = Stack()

    def enque(self, data):
        self.oldstack.push(data)

    def deque(self):
        if self.newstack.is_empty():
            while not self.oldstack.is_empty():
                self.newstack.push(self.oldstack.pop())
        return self.newstack.pop()

    def printqueue(self):
        if not self.newstack.is_empty():
            self.newstack.printstck()
        self.oldstack.printstck()
        print("\n ")
    # def __str__(self):
    #     return self.itemsshow


my = MyQueue()
for i in range(1, 20):
    my.enque(i)
my.printqueue()
my.deque()
my.printqueue()
my.deque()
my.printqueue()
my.deque()
my.printqueue()
my.deque()
my.printqueue()
