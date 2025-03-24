l1 = [5, 6, 7, 5, 8, 9, 6, 10, 6]
# Index can be used to find index of an entry
print(l1.index(6))
print(l1.index(6,2))
# print(l1.index(6,2,6)) # Will give an error as there is no 6 between 2 and 5 index

# Count returns the count of an entry in the list
print(l1.count(6))

# reverse can be used to reverse
l1.reverse()
print(l1)

# sort can be used to sort a list
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

l2 = ['yy','jj','mm','BB','aa','ZZ']
l2.sort()
print(l2)

l2.sort(key=str.lower)
print(l2)