import copy

l = [[1],20,30,40,50]
l1 = copy.copy(l)
l2 = copy.deepcopy(l)

l[0].append(2)
l[0][1] = 1
print(l,l1) # immutable objects will be changed for both
print(l,l2) # not for l2

print(id(l1[0]), id(l[0]))  # same id → shallow copy points to same elements
print(id(l2[0]), id(l[0]))  # same id → deepcopy *still* points to same (if they're immutable) else different

"""
    l1 = copy.copy() points to the same object
    l = [0, 1, 2, 3, 4]
         |  |  |  |  |
         10 20 30 40 50
         |  |  |  |  |
    l1 =[0, 1, 2, 3, 4]
"""

"""
    l2 = copy.deepcopy() creates new object
    l = [0, 1, 2, 3, 4]
         |  |  |  |  |
         10 20 30 40 50

    l2 =[0, 1, 2, 3, 4]
         |  |  |  |  |
         10 20 30 40 50
"""

