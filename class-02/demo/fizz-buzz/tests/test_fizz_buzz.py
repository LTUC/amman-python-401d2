from fizz_buzz import __version__
from fizz_buzz.fizz_buzz_functions import fizz_buzz


def test_version():
    actual = __version__
    expected = '0.1.0'
    assert actual == expected

"""
Test case:
    12 => Fizz
    20 => Buzz
    15 => FizzBuzz
    7  => 7
    0  => FizzBuzz
    '1' => 'Invalid Input'
"""

# def test_name():
#     actual =
#     expected =
#     assert actual == expected

def test_twelve():
    actual = fizz_buzz(12)
    expected = 'Fizz'
    assert actual == expected

def test_twenty():
    actual = fizz_buzz(20)
    expected = 'Buzz'
    assert actual == expected

def test_fifteen():
    actual = fizz_buzz(15)
    expected = 'FizzBuzz'
    assert actual == expected

def test_seven():
    actual = fizz_buzz(7)
    expected = 7
    assert actual == expected

def test_zero():
    actual = fizz_buzz(0)
    expected = 'FizzBuzz'
    assert actual == expected

def test_invalid():
    actual = fizz_buzz('1')
    expected = 'Invalid Input'
    assert actual == expected

def test_float():
    actual = fizz_buzz(1.23)
    expected = 'Invalid Input'
    assert actual == expected
