number = int(input("Enter a number: "))

print(f"Table of {number}")
for i in range (1, 11):
    print(f"{number} X {i} = {number * i}")

factorial_ans = 1

for i in range(1, number+1):
    factorial_ans *= i

print(f"{number}! = {factorial_ans}")
