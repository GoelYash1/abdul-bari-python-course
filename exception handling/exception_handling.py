a = input("Enter numerator: ")
b = input("Enter denominator: ")

try:
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print(f"{a} or {b} cannot be changed to int")
    c = a//b
    print(c)
except ZeroDivisionError:
    print('Zero Division Error')
except TypeError:
    print(f"{type(a)} or {type(b)} is string.")

print('end')