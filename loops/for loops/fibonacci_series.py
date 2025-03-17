n = int(input("Number of terms to generate in fibonacci series: "))

a = 0
b = 1
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c