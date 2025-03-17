number = int(input("Enter a number: "))

count = 0
print("Factors: ")
for i in range(1, (number//2) + 1):
    if number % i == 0:
        count+=1
        print(i)

if count == 2:
    print(f"{number} is a prime number")

