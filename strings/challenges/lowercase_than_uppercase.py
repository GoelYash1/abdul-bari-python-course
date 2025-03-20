s = input("Enter a string in uppercase and lowercase mixed: ")

low = up = ""

for char in s:
    if char.islower():
        low+=char
    else:
        up+=char

ans = low + up
print(ans)