# put your array_reverse challenge tests here
from data_structures_and_algorithms.challenges.array_reverse import reverse_array

# here's a test to get you started
def test_reverse_array():
    actual = reverse_array([1, 2, 3, 4, 5, 6])
    expected = [6, 5, 4, 3, 2, 1]
    assert actual == expected
