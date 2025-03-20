s1 = input("Enter a string: ")
s2 = input("Enter another string: ")


if len(s1)!=len(s2):
    print("Not Anagram")
else:
    for x in s1.lower():
        if x not in s2.lower():
            print("Not Anagram")
            break
    else:
        print("Anagram")