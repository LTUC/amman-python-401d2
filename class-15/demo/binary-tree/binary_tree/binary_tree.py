class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def preorder(self):
        #1. Initialize
        output = []

        #2. Define the closure
        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        #3. Call the closure with initial value
        _walk(self.root)

        #4. Return the result
        return output

        # self.output.append(self.root.value)
        # if self.left:
        #     self.preorder(self.left)
        # if self.right


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    print(bt.preorder())


    #         6
    #     -1      5
    #   10      7   3
