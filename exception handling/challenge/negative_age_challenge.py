class ZeroNegativeAgeError(Exception):
    def __init__(self):
        self.msg = 'Age cannot 0 or -ve'
    def __str__(self):
        return self.msg

def stage(age):
    if age<=0:
        raise ZeroNegativeAgeError
    elif 0<age<13:
        print('Kid')
    elif 13<=age<20:
        print('Teen')
    elif 20<=age<50:
        print('Young')
    else:
        print('Old')
age = int(input("Enter a age: "))
try:
    stage(age)
except ZeroNegativeAgeError as e:
    print(e)