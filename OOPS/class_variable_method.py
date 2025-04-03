class Rectangle:
    count = 0
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count+=1

    def perimeter(self):
        return 2 *(self.breadth + self.length)

    def area(self):
        return self.breadth * self.length

    @classmethod
    def countRect(cls):
        print(cls.count)

    @staticmethod
    def issquare(length, breadth):
        return length == breadth
r1 = Rectangle(10,5)
r2 = Rectangle(8,6)

Rectangle.countRect()
r1.countRect()
r2.countRect()

# Static methods are not related to an instance
print(Rectangle.issquare(10,20))
print(Rectangle.issquare(10,10))