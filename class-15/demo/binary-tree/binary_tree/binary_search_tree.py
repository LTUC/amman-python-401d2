from binary_tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    # go left
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    # go right
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
            _walk(self.root)

    def contains(self, value):
        pass



if __name__ == '__main__':
    # 4,9,-1,6,3,8,5
        #     4
        #   /    \
        # -1      9
        #   \    /
        #   3   6
        #      / \
        #     5   8

    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)

    assert bst.root.value == 4
    assert bst.root.left.value == -1
    assert bst.root.right.value == 9
    assert bst.root.left.right.value == 3
    assert bst.root.right.left.left.value == 5
    print('=====All passed======')

