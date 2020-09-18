"""
3.1 Three in One: Describe how you could use a single array to implement three stacks.
"""
"""
We can allocate 1/3rd of array to the each stack and operate it normally --> but one of therm may overflow without 
using full potentil of array --:
In this case we have to design the structure such that it shifts the elements so as to always have sapce until array 
exhausts
"""
"""
In python we do have a list datastructure --> that can be used to imitate Stacks --> and we do not have a Array like
C ==> so--;);)
"""


class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop(-1)


