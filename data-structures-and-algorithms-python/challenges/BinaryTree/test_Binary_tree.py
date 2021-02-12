from BinaryTree import breadth_first_traversal
from data_structure.tree.tree import BinaryTree , Node

def test_breadth():
   
    Binary_tree = BinaryTree()
    Binary_tree.root = Node(6)
    Binary_tree.root.right = Node(5)
    Binary_tree.root.left = Node(-1)
    assert Binary_tree.breadth_first_traversal() == [6,5,-1]
