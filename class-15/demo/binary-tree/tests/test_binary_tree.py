import pytest

from binary_tree import __version__
from binary_tree.binary_tree import BinaryTree, Node
def test_version():
    assert __version__ == '0.1.0'

def test_preorder(prep):
    actual = prep.preorder()
    expected = [6,-1,10,5,7,3]
    assert actual == expected

@pytest.fixture
def prep():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    return bt
