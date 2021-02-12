  
import pytest

from tree_intersection import tree_intersection as ti
from data_structures_and_algorithms_python.data_structure.tree.tree import BinaryTree as BT


bt1 = BinaryTree()
root = Node(10)
bt1.root = root
root.left = Node(11)
root.right = Node(12)
root.left.left = Node(9)
root.left.right = Node(15)
root.left.left.left = Node(3)
root.right.left = Node(1)
root.right.right = Node(7)
bt1.breadth_fisrt()

bt2 = BinaryTree()
root = Node(11)
bt2.root = root
root.left = Node(9)
root.right = Node(15)
root.left.left = Node(7)
root.left.right = Node(2)
root.left.right.left = Node(1)
root.left.right.right = Node(8)
root.right.left = Node(3)
root.right.right = Node(4)
bt2.breadth_fisrt()


def test_tree_intersection_exists():
    tree_intersection


def test_binary_tree_exists():
    BinaryTree


def test_tree_intersection_pass():
    actual = tree_intersection(bt1, bt2)
    expected = [11,9,15,7,3,1]
    assert actual == expected


def test_tree_intersection_fail():
    actual = tree_intersection(bt1, bt2)
    expected = [11,9,15,1,7,3,8]
    assert actual != expected