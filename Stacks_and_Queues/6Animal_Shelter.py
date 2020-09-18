"""
3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.You may use the built-in Linked List data structure.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.head = None
        self.end = None

    def enque(self, data):
        if self.head is None:
            self.head = Node(data)
            self.end = self.head
        else:
            self.end.next = Node(data)
            self.end = self.end.next

    def dequeueAny(self):
        if self.head is None:
            print("No Animals in Shelter")
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def dequeueDog(self):
        temp = self.head
        t2 = temp.next
        if temp.data == "DOG":
            self.head = self.head.next
            return "DOG"
        else:
            while t2 is not None:
                if t2.data == "DOG":
                    temp.next = t2.next
                    return "DOG"
                else:
                    t2 = t2.next
                    temp = temp.next
            print("Sorry No Dog in Shelter :)")
            return

    def dequeueCat(self):
        temp = self.head
        t2 = temp.next
        if temp.data == "CAT":
            self.head = self.head.next
            return "CAT"
        else:
            while t2 is not None:
                if t2.data == "CAT":
                    temp.next = t2.next
                    return "CAT"
                else:
                    t2 = t2.next
                    temp = temp.next
            print("Sorry No CAT in Shelter :)")
            return


Ashelter = AnimalShelter()
Ashelter.enque("DOG")
Ashelter.enque("CAT")
Ashelter.enque("CAT")
Ashelter.enque("DOG")
Ashelter.enque("CAT")
Ashelter.enque("DOG")

print(Ashelter.dequeueAny())
print(Ashelter.dequeueDog())
print(Ashelter.dequeueCat())
print(Ashelter.dequeueCat())
print(Ashelter.dequeueCat())
print(Ashelter.dequeueCat())
