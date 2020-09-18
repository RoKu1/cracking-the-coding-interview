class Stack:
    def __init__(self):
        self.items = []
        self.mins = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, data):
        self.items.append(data)
        if not self.mins:
            self.mins.append(data)
            return
        if self.mins[-1] > data:
            self.mins.append(data)
        else:
            self.mins.append(self.mins[-1])

    def pop(self):
        self.mins.pop(-1)
        return self.items.pop(-1)

    def min(self):
        return self.mins[-1]

    def printstack(self):
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i])


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enque(self, data):
        self.items.append(data)

    def deque(self):
        return self.items.pop(0)

    def printqueue(self):
        for i in range(0, len(self.items)):
            if i == (len(self.items) - 1):
                print(self.items[i])
            else:
                print(self.items[i], end=" -> ")
