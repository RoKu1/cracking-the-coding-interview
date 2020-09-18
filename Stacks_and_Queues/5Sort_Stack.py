"""
3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""
from Stacks_and_Queues import Stack_and_Queue as SQ


def sortstack(stack):
    if stack.is_empty():
        return stack
    temstack = SQ.Stack()
    temstack.push(stack.pop())
    while not stack.is_empty():
        temp = stack.pop()
        if temstack.peek() >= temp:
            temstack.push(temp)
        else:
            while not temstack.is_empty():
                if temstack.peek() < temp:
                    stack.push(temstack.pop())
                else:
                    break
            temstack.push(temp)
    temstack.printstack()
    return temstack


stack = SQ.Stack()
for i in range(1, 10):
    stack.push(i)

stack.printstack()
sortstack(stack)
