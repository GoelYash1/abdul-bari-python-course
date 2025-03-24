l1 = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

l2 = [
    [5,6,7,8],
    [5,6,7,8],
    [5,6,7,8]
]

l3 = []

for i in range(len(l1)):
    r_list = []
    for j in range(len(l1[i])):
        r_list.append(l1[i][j] + l2[i][j])
    l3.append(r_list)

print(l3)