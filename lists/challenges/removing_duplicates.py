a_list = [int(x) for x in input("Enter space separated integers: ").split()]
ans_list = []

for x in a_list:
    if x not in ans_list:
        ans_list.append(x)

print(ans_list)