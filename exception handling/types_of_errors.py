"""
    1. Syntax Error
    2. Logical Error
    3. Runtime Error
"""

# SyntaxError
a = int(input("Enter the value of A: "))
# b = input("Enter the value of B) unterminated string lateral (SyntaxError)
b = int(input("Enter the value of B: "))

# if a > b # SyntaxError
if a>b:
    print(a)
else:
    # print(a) # Logical Error (done by you)
    # Debugger may help in removing logical error
    print(b)

# TypeError (type of runtime error)
c = a // b # type are string they should be float or int (now corrected)
print(c)
