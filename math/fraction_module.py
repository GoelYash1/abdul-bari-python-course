import fractions

f1 = fractions.Fraction(1,2)
f2 = fractions.Fraction(0.2).limit_denominator(10)
print(f2)
print(f1)

print("Operations on fractions: ")
print("Add:",f1+f2)
print("Sub:",f1-f2)
print("Mul:",f1*f2)
print("Div:",f1/f2)

l = [(1,2),(3,7),(6,8)]

# It will divide the fractions to its simplest form
for i in range(len(l)):
    p,q = l[i]
    print(fractions.Fraction(p,q))