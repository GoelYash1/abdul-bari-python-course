# This function calculates volume of cuboid
def volume(l,b,h): # l, b, h are formal arguments
    return l*b*h

v1 = volume(10,b=5,h=3)
'''
    v2 = volume(10,b=5,3) # Not allowed because positional argument should be first then keyword arguments 
    v3 = volume(l=10,5,k=3) # same reason with formal argument name wrong
'''
v4 = volume(10,5,h=3)