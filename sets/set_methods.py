s1 = {10, 20, 30, 40, 50}
print(s1)

s1.add(60)
print(s1)

# Shallow Copy of s2 i.e changing s2 or s1 does not change the other set
s2 = s1.copy()

# Update can be used to add multiple elements
s1.update({60,40,50})

# For removing
# Pop will remove one element from the set but we don't know which one
s1.pop()
print(s1)

# discard can be used to discard a element from s1
s1.add(20)
s1.discard(20)
print(s1)

'''# Remove will remove like discard but will throe error
s1.remove(20) # Key Error'''

# Clear will clear the set
s1.clear()
print(s1)

