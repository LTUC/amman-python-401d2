
# from data_structure.stacks_and_queues.stacks_and_queues import Queue


class Node:
    def __init__(self,value ):
        self.value  = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None 

    def preorder(self):
        array_of_output = [] 
        def _walk(node):
            array_of_output.append(node.value)
            if node.left:
               _walk(node.left)
            if node.right:
               _walk(node.right)  
        _walk(self.root)  
 
        return array_of_output 

    def inOrder(self):
        array_of_output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            array_of_output.append(node.value)
            if node.right:
                _walk(node.right)
            return array_of_output

        if self.root:    
            _walk(self.root)
        return array_of_output

    def postOrder(self):
        array_of_output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            array_of_output.append(node.value)
            return array_of_output

        if self.root:    
            _walk(self.root)

        return array_of_output

    def max_value(self , root):  
        if self.root:
           max_number = self.root.value
        def _closure(node):
            max_number = self.root.value
            if node:
                if node.value > max_number:
                    max_number = node.value
                _closure(node.left)
                _closure(node.right)
                return max_number       

        _closure(self.root)
        return max_number

    def  breadth_first_traversal(self, root):
        output = []
        if self.root:
           breadth = Queue()
           breadth.enqueue(self.root)
        while breadth.peek():
            front = breadth.dequeue()
            output.append(front.value)
            if front.left != None:
                breadth.enqueue(front.left)

            if front.right != None:
                breadth.enqueue(front.right)   
        return output         



# ------------------------------------
class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return 
                    else:
                        _walk(node.left) 
                else:
                    if not node.right:
                        node.right = Node(value)
                        return 
                    else:
                        _walk(node.right)
                _walk(self.root)

    def contains(self, value):
        if self.root.value == value:
            return True
        elif self.root.value < value:
            return self.root.right.value == value 
        else:
            return self.root.right.value == value      
    
# ===========================
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            self.rear.next= node
            self.rear = node
        else:
            self.front =node
            self.rear = node    

    def dequeue(self):
        if self.front:
            removed_front = self.front
            self.front = self.front.next
            return removed_front
        else:
            raise AttributeError('The Queue is empty')

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'There is no any peek becasue the Queue is empty'    


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    print(bt.preorder())
    print(bt.max_value(bt.root))
 



