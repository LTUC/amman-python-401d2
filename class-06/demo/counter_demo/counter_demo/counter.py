from collections import Counter
import random

count = Counter([7,3,2,7,7,'a','b','a'])

print(count[7])
print(count['a'])

count2 = Counter([1,2,1,4,4,1])
print(count2.most_common())
print(count2.most_common(1))
print(count2.most_common(2))

dice = [random.randint(1,6) for i in range(6)]

# dice = []
# for i in range(6):
#     dice.append(random.randint(1,6))

dice_count = Counter(dice)
dice_count.most_common(1)[0][1]
# if the above returns 1, what does that mean?
# Answer: [(3,1),(4,1),(2,1),(5,1),(1,1),(6,1)]

pets = ['cat', 'dog', 'turtle', 'cat', 'cat', 'turtle']
pets_counter = Counter(pets)
print(pets_counter.most_common())
print(pets_counter.most_common(1))
print(pets_counter.most_common(2))


# Straight [(3,1),(4,1),(2,1),(5,1),(1,1),(6,1)]
d = Counter([3,2,4,5,1,6])
print(d.most_common(1)[0][1]) # if this is 1 then stright 1500 points
