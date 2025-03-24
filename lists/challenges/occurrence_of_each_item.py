l1 = input("Enter characters space separated: ").split()
l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)
        l2.append(l1.count(x))

print(l2)