class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class StackNode:
    def __init__(self):
        self.top = None

    def push(self, val):
        newNode = Node(val)

        if self.top:
            newNode.next = self.top
            self.top = newNode
        else:
            self.top = newNode

    def pop(self):
        if self.top:
            curr = self.top
            self.top = self.top.next
            return curr
        else:
            return None

    def print(self):
        curr = self.top
        while curr:
            print(curr.val)
            curr = curr.next


stack = StackNode()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.pop()
stack.print()