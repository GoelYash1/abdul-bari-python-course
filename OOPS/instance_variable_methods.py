class Test:
    def __init__(self):
        self.a = 10

    def fun(self):
        self.b = 20

# Created instance variable a by init method
t1 = Test()

# Created instance variable b by calling instance method fun
t1.fun()

# Created instance variable c from main
t1.c = 30

print(dir(t1))