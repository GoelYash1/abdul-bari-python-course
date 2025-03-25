a,a1 = {1, 2, 3, 5, 7},{1, 2, 3, 5, 7}
b,b1 = {5, 7, 9, 10, 11},{5, 7, 9, 10, 11}

c = a.union(b)
d = a.intersection(b)
e = a.difference(b)
f = b.difference(a)
g = a.symmetric_difference(b)

print("Set a:", a)
print("Set b:", b)
print(f"Union: {c}")
print(f"Intersection: {d}")
print(f"Difference a-b: {e}")
print(f"Difference b-a: {f}")
print(f"Symmetric Difference a^b: {g}")

a.intersection_update(b)
b.intersection_update(a1)

print(a)
print(b)

a = {1,2,3,4,5,6,7,8,9,10}
b = {1,2,3,5,7}
c = {4,6,8,10}

print(f"Is b a subset of a: {b.issubset(a)}")
print(f"Is c a subset of a: {c.issubset(a)}")
print(f"Is a a superset of b: {a.issuperset(b)}")
print(f"Is b and c disjoint sets: {b.isdisjoint(c)}")