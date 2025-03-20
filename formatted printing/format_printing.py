a = 22
b = 7
c = a/b
d = 23.2323424

print("division of {} and {} is {}".format(a,b,c))
print("division of {0} and {1} is {2}".format(a,b,c))
print("division of {0:10} and {1:15} is {2:2.4}".format(a,b,c))
print("division of {0:<10} and {1:^15} is {2:.4}".format(a,b,c))
# < left aligned ^ center aligned {2:2.4} means 2 means total space which is less than 5 (including decimal) so nothing will be effected and 4 total digits
print("{0:5.4}".format(d))
x = 1234567890

print('{0:10,}'.format(x))

# New way is using like this
print(f"Division of {a:10} and {b:^15} is {c:2.4}")
print(f"{x:G}") # makes big ints like x using E i.e 1234567890 = 1.23457E+09 (E+09) means 10^9

# THERE ARE MORE WAYS TO FORMAT A STRING WHICH CAN BE LOOKED UPON LATER
