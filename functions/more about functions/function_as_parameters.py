def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def arithmetic(f,x,y):
    return f(x,y)

a = 5
b = 3
sum_a_b = arithmetic(add,a,b)
diff = arithmetic(minus,a,b)
print(f"Sum of {a} and {b}: {sum_a_b}")
print(f"Difference of {a} and {b}: {diff}")