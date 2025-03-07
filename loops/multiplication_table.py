number = int(input("Enter a number: "))

count = 1
print(f"The table of {number} is: ")
while count <= 10:
    print(f"{number} X {count} = {number * count}")
    count+=1