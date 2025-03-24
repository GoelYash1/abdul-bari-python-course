fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

min_sum = int(2 * len(fav1) + 1)
ans = ""
for i in range(0,len(fav1)):
    ele_sum = i + fav2.index(fav1[i])
    if ele_sum < min_sum:
        min_sum = ele_sum
        ans = fav1[i]

print(ans,min_sum)

