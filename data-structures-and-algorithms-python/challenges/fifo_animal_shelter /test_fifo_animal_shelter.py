from fifo_animal_shelter import Queue, Node, Dog, Cat, AnimalShelter

def test_queue_exist():
    assert Queue

def test_animal_shelter_exist():
    assert AnimalShelter

def test_cat():
    assert Cat

def test_dog():
    assert Dog

def test_enqueue_cat():
    shelter1 = AnimalShelter('shelter1')
    cat1 = Cat('cat1')
    cat2 = Cat('cat2')
    cat3 = Cat('cat3')
    shelter1.enqueue(cat1)
    shelter1.enqueue(cat2)
    shelter1.enqueue(cat3)
    assert shelter1


def test_dequeue_cat():
    shelter1 = AnimalShelter('shelter1')
    cat1 = Cat('cat1')
    cat2 = Cat('cat2')
    cat3 = Cat('cat3')
    shelter1.enqueue(cat1)
    shelter1.enqueue(cat2)
    shelter1.enqueue(cat3)
    assert shelter1.dequeue('cat').name == 'cat1'


def test_enqueue_dog():
    shelter1 = AnimalShelter('shelter1')
    dog1 = Dog('dog1')
    dog2 = Dog('dog2')
    shelter1.enqueue(dog1)
    shelter1.enqueue(dog2)
    assert shelter1


def test_dequeue_dog():
    shelter1 = AnimalShelter('shelter1')
    dog1 = Dog('dog1')
    dog2 = Dog('dog2')
    shelter1.enqueue(dog1)
    shelter1.enqueue(dog2)
    assert shelter1.dequeue('dog').name == 'dog1'


def test_enqueue_cats_and_dogs():
    shelter2 = AnimalShelter('shelter2')
    dog1 = Dog('dog1')
    cat1 = Cat('cat1')
    dog2 = Dog('dog2')
    cat2 = Cat('cat2')
    shelter2.enqueue(dog1)
    shelter2.enqueue(cat1)
    shelter2.enqueue(dog2)
    shelter2.enqueue(cat2)
    assert shelter2


def test_dequeue_cats_and_dogs():
    shelter2 = AnimalShelter('shelter2')
    dog1 = Dog('dog1')
    cat1 = Cat('cat1')
    dog2 = Dog('dog2')
    cat2 = Cat('cat2')
    shelter2.enqueue(dog1)
    shelter2.enqueue(cat1)
    shelter2.enqueue(dog2)
    shelter2.enqueue(cat2)
    assert shelter2.dequeue('cat').name == 'cat1'
    assert shelter2.dequeue('dog').name == 'dog1'