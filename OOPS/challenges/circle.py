import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2),2)

    def perimeter(self):
        return round(2* math.pi * self.radius,2)

c1 = Circle(7)
print(f"Area: {c1.area()}")
print(f"Perimeter: {c1.perimeter()}")