class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enq(self, val):
        newNode = Node(val)

        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def deque(self):
        if self.front is None:
            print('Nothing to remove')
        else:
            curr = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return curr.val

    def isEmpty(self):
        return self.front is None

    def print(self):
        if self.front is None:
            print('Nothing to print')
        curr = self.front
        while curr:
            print(curr.val)
            curr = curr.next


que = Queue()
que.enq(10)
que.enq(20)
que.enq(30)
que.enq(40)
que.enq(50)
que.deque()
que.print()