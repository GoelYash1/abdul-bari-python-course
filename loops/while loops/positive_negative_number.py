num_of_nos = int(input("Enter number of numbers: "))

total_sum = pos_sum = neg_sum = 0
i = 0
max_num = float('-inf')
while i < num_of_nos:
    num = int(input("Enter a number: "))
    pos_sum+=max(0, num)
    neg_sum+=min(0, num)
    max_num = max(max_num, num)
    i+=1
total_sum = pos_sum + neg_sum
print(max_num)

print(total_sum, pos_sum, neg_sum)

