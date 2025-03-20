punct = '''!()-[]{};:;'"\,<>./?@#$%^&*_~`'''

s = input("Enter a string: ")

ans = ""

for char in s:
    if char not in punct:
        ans+=char

print(ans)