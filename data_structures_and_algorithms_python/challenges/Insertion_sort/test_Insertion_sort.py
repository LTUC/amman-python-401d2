from Insertion_sort import InsertionSort


def test_Insertion_sort():
    actual = InsertionSort([2,4,0,3])
    expected = [0,2,3,4]
    assert actual == expected