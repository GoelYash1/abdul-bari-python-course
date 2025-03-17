a = int(input("Enter the first term of an arithmetic progression: "))
d = int(input("Enter the difference between two consecutive terms in AP: "))

n = int(input("Number of terms to print: "))

for t in range(a, a+n*d, d):
    print(t)
