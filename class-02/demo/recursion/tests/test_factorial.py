from recursion.factorial import fact

def test_five():
    actual = fact(5)
    expected = 5*4*3*2*1
    assert actual == expected

def test_one():
    actual = fact(1)
    expected = 1
    assert actual == expected

def test_zero():
    actual = fact(0)
    expected = 1
    assert actual == expected
