from data_structure.tree.tree import Node , BinaryTree , BinarySearch
from data_structure.stacks_and_queues.queue_with_stack import Queue


def  breadth_first_traversal(root):
    breadth = Queue()
    breadth.enqueue(root)
    while breadth.peek():
        self.front = breadth.dequeue
        if self.front.left != None:
            breadth.enqueue(self.front.left)

        if self.front.right != None:
            breadth.enqueue(self.right)    
