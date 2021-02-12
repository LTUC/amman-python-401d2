class Node:
  
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    
    def dequeue(self):
        if self.front:
            temp = self.front
            if self.front.next == None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError('The queue is Empty')


class AnimalShelter:
    def __init__(self, name):
        self.name = name
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal.type == 'cat':
            self.cats.enqueue(animal)
        elif animal.type == 'dog':
            self.dogs.enqueue(animal)
        
    
    def dequeue(self, pref = None):
        if pref == 'cat':
            return self.cats.dequeue()
        elif pref == 'dog':
            return self.dogs.dequeue()


class Cat:
    def __init__(self, name):
        self.name = name
        self.type = 'cat'

class Dog:
    def __init__(self, name):
        self.name = name
        self.type = 'dog'