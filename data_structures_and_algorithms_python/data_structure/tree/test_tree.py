from tree import Node , BinaryTree , BinarySearchTree
import pytest 

@pytest.fixture
def prep():
    Binary_tree = BinaryTree()
    Binary_tree.root = Node(3)
    Binary_tree.root.right = Node(4)
    Binary_tree.root.left = Node(1)
    Binary_tree.root.right.left = Node(2)
    return Binary_tree


def test_preorder(prep):
    actual = prep.preorder()  
    expected = [3,1,4,2]  
    assert actual == expected 

def test_contains():
    Binary_tree = BinarySearchTree()
    Binary_tree.add(2)
    assert Binary_tree.root.value == 2
    

def test_tree_inorder():
    Binary_tree = BinaryTree()
    Binary_tree.root = Node(6)
    Binary_tree.root.right = Node(5)
    Binary_tree.root.left = Node(-1)
    Binary_tree.root.right.left = Node(7)
    Binary_tree.root.left.left = Node(10)
    Binary_tree.root.right.right = Node(3)
    assert Binary_tree.inOrder() == [10, -1, 6, 7, 5, 3]

def test_tree_postorder():
    Binary_tree = BinaryTree()
    Binary_tree.root = Node(6)
    Binary_tree.root.right = Node(5)
    Binary_tree.root.left = Node(-1)
    Binary_tree.root.right.left = Node(7)
    Binary_tree.root.left.left = Node(10)
    Binary_tree.root.right.right = Node(3)
    assert Binary_tree.postOrder() == [10, -1, 7, 3, 5, 6]


def test_max_value():
    Binary_tree = BinaryTree()
    Binary_tree.root = Node(6)
    Binary_tree.root.right = Node(5)
    Binary_tree.root.left = Node(-1)
    assert Binary_tree.max_value(Binary_tree.root) == 6

