# AnimalShelter class
enqueue(animal) ==> animal could be cat or dog
dequeue(pref)  ==> shelter.dequeue('cat') or shelter.dequeue('dog') or shelter.dequeue()

class Cat:
    pass

class Dog:
    pass

shelter = AnimalShelter()
shelter.enqueue(Cat('Sherry'))
shelter.enqueue(Cat('Instance'))
shelter.enqueue(Dog('Alex'))
shelter.enqueue(Dog('JJ'))

dequeue() ==> 'Sherry'
dequeue('dog') ==> 'Alex'
dequeue('dog') ==> 'JJ'
