# Dictionary can be created like this
dict1 = dict()
dict2 = {}

# Iterable pairs dictionary
dict3 = dict((["Name", "Yash"],["Roll Number",30026933]))
print(dict3)

# By using zip functon
l1 = ['A','B','C']
l2 = ['Apple','Ball','Cat']
dict4 = dict(zip(l1,l2))
print(dict4)

# Enumerate can be used to add to a dictionary
l1 = ['Yash Goel', 'Shubham Kumar', 'Nitin Sharma']
dict5 = dict(enumerate(l1))
print(dict5)

# By following this way dict6 = {exp:exp for item in iterable}
dict6 = {item:item**2 for item in range(10)}
print(dict6)

dict7 = dict((item,item**2) for item in range(10))
print(dict7)

l1 = [1,2,3]
l2 = ['A','B','C']

dict8  = dict((x,y) for x,y in zip(l1,l2))
print(dict8)

dict9  = {x: y for x,y in zip(l1,l2)}
print(dict9)

dict10 = {x:y for x,y in enumerate(l2)}
print(dict10)
