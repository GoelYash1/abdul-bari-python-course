s = input("Enter a string: ")
rev = s[::-1]
s2=""
if s == rev:
    print(f"String {s} is a palindrome")
else:
    s2 = s + rev
    print(f"String {s2} is now a palindrome")
