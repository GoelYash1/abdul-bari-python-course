# With default arguments
def volume_of_cuboid(l=1,b=1,h=1): # Default arguments should be filled from the right hand side
    v = l*b*h
    return v

v1 = volume_of_cuboid(10,5,3)
v2 = volume_of_cuboid(10,5)
v3 = volume_of_cuboid(10)
v4 = volume_of_cuboid()

# ANY TYPE OF ARGUMENT CAN BE TAKEN AS ARGUMENT
# v.v important
def fun(l = [1,2,3]):
    l.append(len(l))
    print(l)

fun()
fun()
fun([10,11])
fun()

'''
    [1,2,3,3]
    [1,2,3,3,4]
    [10,11,2]
    [1,2,3,3,4,5]
    
    Once a default argument is created it uses the same one
'''