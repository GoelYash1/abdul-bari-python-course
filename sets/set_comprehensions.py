# For creating empty set
s = {} # This is a dictionary not a set
s1 = set()

for x in range(1,11):
    s1.add(x)

s2 = {x for x in range(10)}
s3 = {x ** 2 for x in [-2,-1,0,1, 2]}

print(s2)
print(s3)
