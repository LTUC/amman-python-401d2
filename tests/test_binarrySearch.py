from data.challenges.BinarySearch import array_binary_search

def test_arryBinarySearch():
    actual = array_binary_search ([1,3,6,8,9],9)
    expected = 4
    assert actual==expected


def test_arryBinarySearchNegative():
    actual = array_binary_search ([1,3,6,8,9],11)
    expected = -1
    assert actual==expected