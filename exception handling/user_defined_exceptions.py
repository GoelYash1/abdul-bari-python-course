class ZeroNegativeError(Exception):
    def __init__(self):
        self.msg = 'zero or -ve Dimension'
    def __str__(self):
        return self.msg

def area(length, breadth):
    if length >0 and breadth>0:
        a = length * breadth
        return a
    else:
        raise ZeroNegativeError

print(area(10,5))
print(area(1,-3))