from hashtable import Hashmap 



def test_Hashmap_default_size():
    hash = Hashmap(1024)
    actual = hash.size
    expected = 1024
    assert actual == expected


def test_single_hash():
    hash = Hashmap()
    hash.add('could', 45)
    actual = hash.Get_hash('could')
    expected = 903
    assert actual == expected


def test_contains():
    hash = Hashmap()
    hash.add('could', 65)
    expected = hash.contains('could')
    actual = True
    assert actual == expected

def test_contains_collsion():
    hash = Hashmap()
    hash.add('could', 40)
    hash.add('colud', 33)
    hash.add('cludo', 11)
    expected = hash.contains('cludo')
    actual = True
    assert actual == expected


def test_is_not_contains_collsion():
    hash = Hashmap()
    hash.add('could', 40)
    expected = hash.contains('saja')
    actual = True
    assert actual != expected


def test_add_multiple_hash():
    hash = Hashmap()
    hash.add('could', 45)
    hash.add('cludo', 33)
    hash.add('colud', 11)
    actual = hash.Get_hash('colud')
    expected = 903
    assert actual == expected
