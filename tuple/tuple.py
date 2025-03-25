# tuple can be created in multiple ways
# TUPLE IS IMMUTABLE
t1 = 1,2,3,4,5
print(f"t1: {t1}")
t2 = tuple((1,2,3,4,5))
print(f"t2: {t2}")
t3 = (1,2,3,4,5)
print(f"t3: {t3}")

# Tuple cam be created like this as well
t4 = tuple(x for x in range(10))
t5 = (*(x for x in range(10)),)

'''
    tuple has packing and unpacking capabilities
    like t1 is packed to a tuple (1,2,3,4,5)
'''
a,b,c,d,e = t1 # unpacking

print(t1)
print(a,b,c,d,e)

'''* means taking all the remaining one but only one star expression is allowed'''
x,y,*z = t1
print(x,y,z)

'''
x,*y,*z = t1 # Not allowed
print(x,y,z)
'''