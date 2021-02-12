from fizz_buzz_tree import FizzBuzzTree , BinaryTree , Node

import pytest

def test_fizz_buzz():
    bt = BinaryTree()
    bt.root = Node(3)
    bt.root.right = Node(5)
    bt.root.left = Node(15)
    bt.root.left.left = Node(1)
    actual = FizzBuzzTree(bt)
    expect = ['Fizz','FizzBuzz',1, 'Buzz']
    assert actual == expect

