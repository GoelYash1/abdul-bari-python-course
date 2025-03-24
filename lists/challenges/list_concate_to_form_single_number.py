l1 = [int(x) for x in input("Enter space separated numbers: ").split()]

ans = ""
for x in l1:
    ans+=str(x)
print(int(ans))