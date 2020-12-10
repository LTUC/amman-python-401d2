from stacks_queues.node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        # return some data
        pass

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

    def is_empty(self):
        pass


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.peek())
