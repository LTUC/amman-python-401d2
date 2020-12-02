from pets_shelter import __version__
from pets_shelter.pets import Pet, Dog, Cat

def test_version():
    assert __version__ == '0.1.0'
