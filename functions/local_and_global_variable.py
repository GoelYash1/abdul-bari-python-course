g=5.25
print("Outside - 1: ",g)

def fun():
    global g # Without this Outside - 2 will print 5.25
    a=10
    g = 199
    print("local: ",a)
    print("global: ",g)

def fun2():
    a,b,c = 1,2,3
    print(locals())
    print(globals()) # It will also have already declared global variables

fun()
fun2()
print("Outside - 2: ",g)
