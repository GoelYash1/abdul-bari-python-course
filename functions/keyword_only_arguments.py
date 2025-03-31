def fun(a,b,*,c,d): # * is used to separate key word and normal arguments, the right one are key word only
    print(a,b,c,d)

# * cannot be at the end def fun(a,b,c,d,*) as one should be at least on the right
'''
    print(fun(1,2,3,4)) # c and d should be key word based
'''
print(fun(1,2,c=4,d=5))
print(fun(1,2,d=4,c=5))
