items = [1,2,[3,4,[5,6],7],8]

def flatten(l):
    for e in l:
        if type(e) == list:
            yield from flatten(e)
        else:
            yield e

print(f"List 1 is not flattened, {items}")
f = list(flatten(items))
print("flattened list: ", f)

print(f"\nList 2 is already flattened, {[1,2,3,4,5,89]}")
f2 = flatten([1,2,3,4,5,89])
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
