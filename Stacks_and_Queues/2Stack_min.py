"""
3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum eiement? Push, pop and min should ail operate in 0 ( 1 ) time.
"""
"""
Solution --> keep track of what is min at each stage of opertaion 
"""


class Stack:
    def __init__(self):
        self.items = []
        self.mins = []

    def is_empty(self):
        return self.items == []

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


stack = Stack()
stack.push(2)
stack.push(5)
stack.push(1)
print(stack.min())
stack.pop()
print(stack.min())
