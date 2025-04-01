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

"""
    proper structuring is
    try:
        something()
    except:
        some error in something
    else:
        print(something if try has no errors)
    finally:
        do something regardless
"""