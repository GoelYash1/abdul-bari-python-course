import heapq

def kth_largest(h, k):
    # Create a max-heap by negating the values
    negative_heap = [-x for x in h]
    heapq.heapify(negative_heap)

    # Pop (k-1) elements to get to the k-th largest
    for _ in range(k - 1):
        heapq.heappop(negative_heap)

    # The k-th largest is now at the top
    print(-heapq.heappop(negative_heap))

k = int(input("Which largest element do you want to find: "))
l = [10, 29, 64, 90, 82, 74, 33]

kth_largest(l, k)
