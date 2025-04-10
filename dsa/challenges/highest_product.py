import heapq

t = int(input("Enter the number of test cases: "))


def pair_with_highest_product(arr):
    if len(arr) < 2:
        return "Not Possible"

    two_largest = heapq.nlargest(2, arr)
    two_smallest = heapq.nsmallest(2, arr)

    prod_two_largest = two_largest[0] * two_largest[1]
    prod_two_smallest = two_smallest[0] * two_smallest[1]

    if prod_two_largest > prod_two_smallest:
        return two_largest
    else:
        return two_smallest


while t > 0:
    t -= 1
    nums = list(map(int, input("Enter numbers: ").split()))
    result = pair_with_highest_product(nums)
    print("Pair with highest product:", result)
