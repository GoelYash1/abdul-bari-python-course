def count(s=""):
    up_count,lower_count = 0,0
    for c in s:
        if c.islower():
            lower_count+=1
        if c.isupper():
            up_count+=1
    return lower_count,up_count

ans = count("My name is YASH GOEL")

print(ans)