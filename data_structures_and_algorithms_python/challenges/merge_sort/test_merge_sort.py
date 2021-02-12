from merge_sort import merge_sort

'''
edg cases:
The empty list
An already sorted list
A reverse sorted list
A list consist of the same element
A list contain of negative elements
'''

def test_merge_sort_empty():
    actual = merge_sort([])
    expected = []
    assert actual == expected

def test_merge_sort_already_sorted():
    actual = merge_sort([2,3,4,5])
    expected = [2,3,4,5]
    assert actual == expected

def test_merge_sort_reverse_sorted():
    actual = merge_sort([7,6,4,3,1])
    expected = [1,3,4,6,7]
    assert actual == expected


def test_merge_sort_same_elements():
    actual = merge_sort([7,7,7])
    expected = [7,7,7]
    assert actual == expected  

def test_merge_sort_negative_elements():
    actual = merge_sort([7,-6,4,-3,1])
    expected = [-6,-3,1,4,7]
    assert actual == expected        


