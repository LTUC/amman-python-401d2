import random

# from random import random as ranz


print(random.random()) # random number between 0 and 1 (<1)

print(random.random()*3) # random number between 0 and 3 (<3)

print(random.randint(0,3)) # random int between 0 and 3

print(random.randrange(0,10,3)) # step of 3 rand int

print(dir(random))

a = [1,2,3,4,5]
print(random.shuffle(a))

print(a)
