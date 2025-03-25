s = {1,2,3,4,5,6,7,8,9,10}
a = {1,2,3,5,7}
b = {5,7,9,10,11}

print(f"Union of a and b (a|b): {a|b}")
print(f"Intersection of a and b (a&b): {a&b}")
print(f"Difference of a and b (a-b): {a-b}")
print(f"Difference of b and a (b-a): {b-a}")
print(f"Symmetric Difference of a and b (a^b): {a^b}")

print(f"Is a a subset of s (a<s): {a<s}")
print(f"Is s equals s (s==s): {s==s}")
print(f"Is b a subset of s (b<s): {b<s}")

# In and not in to check whether a element is in set or not