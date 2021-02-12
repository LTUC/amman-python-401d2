from data.challenges.linked_list.linked_list import LinkedList
import pytest

def test_insert():
    list = LinkedList()
    list.insert(9)
    assert list.head.value == 9

def test_insert_Numbers():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    assert list.head.value == 2
    assert list.head.next.value == 1
    assert list.head.next.next == None

def test_includes_true():
    list = LinkedList()
    list.insert(4)
    list.insert(5)
    assert list.includes(5) == True
    assert list.includes(7) == False

def test_str():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    assert list.__str__() == "{ 2 } -> { 1 } -> NULL"