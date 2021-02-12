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

def test_append():
    list = LinkedList()    
    list.append(1)
    list.append(2)
    assert list.head.value == 1
    assert list.head.next.value == 2

def test_insertBefore():
    list = LinkedList() 
    list.append(1)
    list.append(2)
    list.append(3)
    list.insertBefore(1,9) 
    list.insertBefore(2,5)  
    assert list.head.value == 9
    assert list.head.next.value == 1 
    assert list.head.next.next.value == 5
    assert list.head.next.next.next.value == 2
    assert list.head.next.next.next.next.value == 3

def test_insertAfter():
    list = LinkedList() 
    list.append(1)
    list.append(2) 
    list.append(3)     
    list.insertAfter(2,7)
    list.insertAfter(3,8)  
    assert list.head.value == 1
    assert list.head.next.value == 2
    assert list.head.next.next.value == 7
    assert list.head.next.next.next.value == 3
    assert list.head.next.next.next.next.value == 8   

def test_startFromLast():
    list = LinkedList() 
    list.append(1)
    list.append(2) 
    list.append(3) 
    assert  list.startFromLast(0) == 3





