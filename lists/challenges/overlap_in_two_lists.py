l1 = [10, 15, 6, 9, 12, 8, 4]
l2 = [14, 6, 19, 4, 7, 10, 11]
l3=[]
if len(l2) > len(l1):
    for x in l2:
        if x in l1 and x not in l3:
            l3.append(x)
else:
    for x in l1:
        if x in l2 and x not in l3:
            l3.append(x)

print(l3)

