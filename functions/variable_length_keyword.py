def fun(**kwargs):
    for item in kwargs.items():
        if item[0] == 'b':
            print(item[1])

# def fun(**kwargs,a,b): not allowed

def fun2(a,b,**kwargs):
    print(a,b,kwargs)

def fun3(*args, a,b,**kwargs):
    print(args,a,b,kwargs)

fun(a=5,b=10,c=20)
fun2(a=5,b=10,c=20)
fun2(5,10,c=20)
fun3(1,2,3,4,x=5,y=10,a=1,b=2)