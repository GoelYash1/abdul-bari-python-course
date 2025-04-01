class InvalidFormulaException(Exception):
    pass

def evaluate(formula):
    f = formula.split()
    if len(f) < 3:
        raise InvalidFormulaException("Formula should have SPACES ex: 10 - 5")
    if f[1] not in ('+','-','*','/'):
        raise InvalidFormulaException("It should be an operator")
    else:
        a,b,c = f
        a = int(a)
        c = int(c)
        if b == '+':
            res = a+c
        elif b == '-':
            res = a-c
        elif b =='*':
            res = a*c
        else:
            if c == 0:
                raise ZeroDivisionError
            else:
                res = a//c
        return res

try:
    formula = input("Enter the formula Ex: 10 - 4: ")
    print(evaluate(formula))
except InvalidFormulaException as e:
    print(e)
except ZeroDivisionError:
    print("Number is divide by 0")