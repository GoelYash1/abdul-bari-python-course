l1 = [1, 2, 3, 4, 5, 10]

# append is used to append to a list
l1.append(11)
print(l1)

l1[len(l1):] = [12,13,14] # single or multiple entries but always inside a list in itself
print(l1)

# extend can be used to extend a list by multiple entries
l1.extend([10,11,12])
print(l1)

# insert can be used to insert at a index
l1.insert(1,12)
print(l1)
l1[0:0] = [0]
print(l1)

# copy creates a shallow copy of the list
l2 = l1
l3 = l1.copy()

print(id(l1), id(l2), id(l3))
l3.clear()
print(l1) # l3.clear() does not clear l1
l2.clear()
print(l1) # l2.clear() will clear l1