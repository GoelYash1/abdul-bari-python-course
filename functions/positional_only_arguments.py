def fun(a,b,/,c,d): # / makes arguments to the left of it to be positional only and left are like other formal arguments
    print(a,b,c,d)
# NOTE / can't be at the beginning of a function arguments (AS AT LEAST ONE ARGUMENT SHOULD PRECEDE /)
'''
    print(fun(a=1, b=1,c=2,d=3)) # This is wrong as first two should be positional
    print(fun(1, b=1,c=2,d=3)) # This is wrong as first two should be positional
    print(fun(1, 1,c=2,3)) # This is wrong as the key words arguments should be at the end
'''
print(fun(1, 1,c=2,d=3))
print(fun(1, 1,2,3))
