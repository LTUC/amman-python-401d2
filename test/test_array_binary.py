
from array_binary.array_binary import call_function

def test_binary_search():
    expected = 2
    actual = call_function([ 2, 3, 4,8, 10, 40,60],4)
    assert actual == expected

def test_binary_search2():
    expected = 5
    actual = call_function([ 2, 3, 4,8, 10, 40,60],40)
    assert actual == expected
