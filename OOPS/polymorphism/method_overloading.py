class Arith:
    def sum(self,a,b,c=None):
        if c is None:
            return a+b
        else:
            return a+b+c

a = Arith()

print(a.sum(1,2))
print(a.sum(1.5,2.8))
print(a.sum("Hello","World"))
print(a.sum(1+5j,2+3j))
print(a.sum([1,2,3],[2,3,4]))

# With three parameters/arguments
print(a.sum(1,2,3))
