class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        super().__init__(l,b)
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height

c = Cuboid(10,5,4)
print(f"Volume of cuboid is: {c.volume()}")