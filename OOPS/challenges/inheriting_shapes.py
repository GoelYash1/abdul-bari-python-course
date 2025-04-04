import math

class Polygon:
    def __init__(self, no_of_sides, *dimensions):
        self.no_of_sides = no_of_sides
        self.dimensions = dimensions[:no_of_sides]

class Triangle(Polygon):
    def __init__(self, no_of_sides, *dimensions):
        super().__init__(no_of_sides, *dimensions)

    def area(self):
        a,b,c = self.dimensions
        semi_perimeter = (a+b+c) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

t1 = Triangle(3,3,4,5,6,7)
print(f"Area: {t1.area()}")
