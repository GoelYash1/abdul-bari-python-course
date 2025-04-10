import heapq
h = []

heapq.heappush(h,20)
heapq.heappush(h,50)
heapq.heappush(h,10)
heapq.heappush(h,40)
heapq.heappush(h,30)
heapq.heappush(h,60)

print(h)
print(heapq.heappop(h))
print(h)
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))

l2 = [50,30,60,40,70,20,10]
heapq.heapify(l2)

print(heapq.nlargest(2,l2))
print(heapq.nsmallest(2,l2))
print(l2)

# pops smallest and pushes the new one heapreplace
heapq.heapreplace(l2,30)
print(l2)
heapq.heappush(l2,30)
print(l2)
