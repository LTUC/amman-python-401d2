from linked_list import __version__
from linked_list.linked_list import LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_append(prep_ll):
    # head - Node(5) -> Node(7) -> None
    assert prep_ll.head.value == 5
    assert prep_ll.head.next.value == 7
    assert prep_ll.head.next.next == None

def test_length(prep_ll):
    assert len(prep_ll) == 2

@pytest.fixture
def prep_ll():
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    return ll
