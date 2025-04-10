import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_list = []
    for i in range(len(arr)):
        sorted_list.append(heapq.heappop(arr))
    return sorted_list

elements = [11,22,3,14,25,16,17,28,10]

print(f"Sorted List: {heap_sort(elements)}")
