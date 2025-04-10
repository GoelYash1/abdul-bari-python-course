import random

# random.seed(10)
# random.random gives float between 0 and 1
for i in range(3):
    print(round(random.random(),3))

# random.seed(10) -> Using random.seed we can start from the same random numbers
for i in range(3):
    print(round(random.random(),3))

# random.uniform gives float between [a,b)
for i in range(3):
    print(round(random.uniform(1,5),3))

# random.randint gives integer between [a,b]
for i in range(3):
    print(random.randint(11,100))

# random.randrange gives integer with step pass between [a,b]
for i in range(3):
    print(random.randrange(1,10,2))

l = [1,3,5,6,9,11,13]
print(random.choice(l))

"""
    random.choices and random.sample are similar
"""
print(random.choices(l,k=2))
print(random.sample(l,k=3))

print(l)
random.shuffle(l)
print(l)

# Numbers between 0 and 16 using this getrandbits and 4 as 2 ^ 4 = 16, so [0,15]
print(random.getrandbits(4))
print(random.getrandbits(4))
print(random.getrandbits(4))
print(random.getrandbits(4))

