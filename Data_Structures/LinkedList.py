class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def insert_at_the_beginning(self, value):
        newNode = Node(value)
        # If Head is not empty
        if self.head:
            newNode.next = self.head
            self.head = newNode
        # If head is empty
        else:
            self.head = newNode
            self.tail = newNode

    def insert_at_the_end(self, value):
        newNode = Node(value)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def remove_from_beginning(self):
        if self.head:
            self.head = self.head.next
        else:
            print('LinkedList Is Empty')

    def remove_from_the_end(self):
        if self.head.next is None:
            self.head = None
            self.tail = None

        if self.head is None:
           print('Nothing to Remove')
           
        # Initialize prev to self.head and loop through the entire linked list to get to previous of Tail
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        self.tail = curr


    def print(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next


lls = LinkedList()

lls.insert_at_the_end(10)
lls.insert_at_the_end(20)
lls.insert_at_the_end(30)
lls.insert_at_the_beginning(0)
lls.insert_at_the_beginning(-10)
lls.insert_at_the_beginning(-20)
lls.remove_from_beginning()
lls.remove_from_the_end()
lls.print()