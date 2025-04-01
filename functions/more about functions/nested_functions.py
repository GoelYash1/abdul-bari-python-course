# nested functions
def area_of_cuboid(l,b,h):
    def area(x,y):
        return x*y
    return 2 * (area(l,b) + area(b,h) + area(h,l))

print("Area of cuboid with l = 3, b = 4 and h = 5:",area_of_cuboid(3,4,5))