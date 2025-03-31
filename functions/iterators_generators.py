l1 = [1,2,3,4]

it = iter(l1)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

m1 = {1:'a',2:'b'}

it = iter(m1)

# It gives keys only
print(next(it))
print(next(it))

print(range(4)) # Range is a generator function

# GENERATOR FUNCTION
def myrange(n):
    i = 0
    while i<n:
        yield i
        i=i+1
m = myrange(4)
print(next(m))
print(next(m))
print(next(m))
print(next(m))

# print(next(m)) # It will stop iteration here

for i in myrange(len(l1)):
    print(l1[i])

def myDays():
    d = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu','Fri','Sat')
    i = 0
    while True:
        yield d[i]
        i = i+1
        i %= 7

d1 = myDays()

print(next(d1))
print(next(d1))
print(next(d1))
print(next(d1))
print(next(d1))
print(next(d1))
print(next(d1))
print(next(d1))
