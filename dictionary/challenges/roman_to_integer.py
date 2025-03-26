roman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

roman_number = input("Enter a number in roman: ").upper()
ans = 0
prev_char = ''
for c in roman_number:
    if prev_char == '':
        ans+= roman[c]
    else:
        if roman[prev_char] < roman[c]:
            ans-=2*roman[prev_char]
            ans+=roman[c]
        else:
            ans+=roman[c]
    prev_char = c
print(ans)