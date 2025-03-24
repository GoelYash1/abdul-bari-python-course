l1 = [1, 2, 3, 4, 5, 6]

# pop can be used to remove any index by default it removes the last index
l1.pop()
print(l1)

l1.pop(2)
print(l1)

del l1[1]
print(l1)

l1 = [1, 2, 3, 6, 4, 5, 6]

# remove can be used to remove a entry matching the entry
l1.remove(6)
print(l1)

# clear is used to clear the list, same like del l1[:] or l1[:] = []
l1.clear()
print(l1)