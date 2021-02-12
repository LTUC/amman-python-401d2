from multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_one_set():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

def test_multi_bracket_2_sets():
    actual = multi_bracket_validation('{}{}')
    expected = True
    assert actual == expected

def test_multi_bracket_multiple_sets():
    actual = multi_bracket_validation('{}[](){}')
    expected = True
    assert actual == expected

def test_extra_characters_():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_extra_characters2_():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected

def test_wrong_closing():
    actual = multi_bracket_validation('[({}]')
    expected = False
    assert actual == expected

def test_close_before_open():
    actual = multi_bracket_validation('(](')
    expected = False
    assert actual == expected

def test_close_before_open2():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected


def test_close_first():
    actual = multi_bracket_validation('}()[(])')
    expected = False
    assert actual == expected