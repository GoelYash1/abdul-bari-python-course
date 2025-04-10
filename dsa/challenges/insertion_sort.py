import bisect

def insertion_sort(ele):
    sorted_list = []
    for e in ele:
        bisect.insort(sorted_list,e)
    return sorted_list
arr = [2,4,6,8,10,1,3,5,7,9]

print(insertion_sort(arr))
