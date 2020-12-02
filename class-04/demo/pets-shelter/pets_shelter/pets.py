# oscar = {
#     'name': 'Oscar',
#     'age': 2,
#     'sound': 'Whooof'
# }

# milo = {
#     'name': 'Milo Jr',
#     'age': 3,
#     'sound': 'Meooow'
# }


# alex = {
#     'fav_food': 'beef',
#     'age': 67
# }

# print(oscar['name'])
# print(milo['sound'])

from abc import ABC, abstractmethod

class Pet(ABC):
    counter = 0

    def __init__(self, name):
        self.name = name
        Pet.counter += 1

    @abstractmethod
    def speak(self): # Abstract method
        pass

    def greet(self): # Instance method / Regular method
        return('hello')

    # Class Method doesn't require instanitiating an intance
    # Can interact with variables defined on the class level
    @classmethod
    def get_pets_count(cls):
        return(cls.counter)

class Dog(Pet):
    default_age = 1
    fav_food = 'meat'

    def speak(self):
        return f'I am {self.default_age} years old'

    # Static Method doesn't require instanitiating an intance
    # Can NOT interact with variables defined on the class level
    @staticmethod
    def get_characteristics():
        x = 8
        return f'Dogs like to jump! {x} times'

    def __str__(self):
        return f'This is a dog called {self.name}.'

    def __repr__(self):
        return f'<DOG: {self.name}>'

class Cat(Pet):
    fav_food = 'fish'
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return('Meoooow')

# Inheritance

if __name__=='__main__':
    oscar = Dog('Oscar')
    milo = Cat('Milo', 3)
    print(oscar.name)
    print(milo.name)
    print(f'My name is {oscar.name} and I am {oscar.default_age} years old.')
    print(f'My name is {milo.name} and I like to eat {milo.fav_food}.')
    print(oscar.speak())
    print(milo.speak())
    print(Dog.get_characteristics())
    sherry = Cat('Sherry',6)
    print(Pet.get_pets_count())
    print(oscar)




