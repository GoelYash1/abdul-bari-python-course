# Normal functions
def double_f(x):
    return x*2

# Lambda functions
double = lambda x: x * 2

print(double_f(3))
print(double(3))

# With multiple variables
add = lambda x,y:x+y
print(add(5,10))

# Directly calling it
print((lambda x:x*2)(5))

# For different data types
l1 = [1,2,3,4,5,6,7,8,9,10]

f1 = list(filter(lambda x: x%3==0, l1))
f2 = list(map(lambda x: -x, l1))
f3 = list(map(lambda x: x if x%2==0 else -x, l1))

print(f1, f2, f3, sep="\n")

l2 = [[4,2,'Six'],[1,4,'Five'],[2,2,'Four']]
l3 = sorted(l2, key=lambda x: x[0] + x[1])
print(l3)