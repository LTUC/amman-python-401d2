from stacks_queues.node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        # return some data
        pass

    def peek(self):
        return self.top.value

    def is_empty(self):
        pass

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push('cat')
    stack.peek() # returns 'cat'
    # stack.pop() # return 'cat'
    # stack.peek() # return 6
