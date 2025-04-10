from collections import Counter

l = ['Mark','Jonny','David','Mark','Jonny','Mark','James','Mathew']

c = Counter(l)

print(c.items())
print(c.keys())
print(c.values())
print("Update counter with Ajay")
c.update({'Ajay':4})
for i in c.elements():
    print(i)

c.pop('Ajay')

print("After popping Ajay")
for i in c.elements():
    print(i)

c.update({'Ajay':4})
print(c.most_common(1))
print(c.most_common(2))

c.popitem()

print(c.items())
