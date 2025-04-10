import bisect

b = [10,20,20,30,50,60,70,90]
print(b)

# insert at sorted position
bisect.insort(b,35)
print(b)

# bisect.bisect gives the position
print(bisect.bisect(b,20))

# bisect_left gives the position of insertion to the left
print(bisect.bisect_left(b,20))