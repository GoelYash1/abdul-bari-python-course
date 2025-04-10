import array

t = int(input("Enter number of test cases: "))

def missing_num(arr):
    start = arr[0]
    end = arr[-1]
    actual_list = list(range(start, end+1))

    actual_sum = sum(actual_list)
    given_sum = sum(arr)

    return actual_sum - given_sum

while t>0:
    t-=1
    nums = array.array('i', map(int, input("").split()))
    mis_num = missing_num(nums)
    if mis_num != 0:
        print(f"Missing number: {mis_num}")
    else:
        print("No Missing Number")
