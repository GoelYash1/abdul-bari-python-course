class Calculator:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def mul(a,b):
        return a * b

    @staticmethod
    def div(a,b):
        return a / b if b!=0 else "Cannot Divide"

print(Calculator.add(1,2))
print(Calculator.sub(1,2))
print(Calculator.mul(1,2))
print(Calculator.div(1,0))
print(Calculator.div(1,1))