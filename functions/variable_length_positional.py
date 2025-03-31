def fun(*args):
    for x in args:
        if type(x) == int:
            print(x)
def fun2(a,b,*args):
    print(a,b,args)

def fun3(*args,a,b):
    print(a,b,args)

def fun4(*args):
    print(args, len(args))
fun(5,1.25,'hello',15)
fun2(5,1.25,'hello',15) # and b in fun2 are positional arguments only
fun3(5,1.25,'hello',15,a=10,b=20) # a and b in fun3 are key word only arguments

l1 = [1,2,3]
fun4(l1) # Output will be ([1,2,3],) 1
fun4(*l1) # Output will be (1,2,3) 3
