from collections import deque

l = [1,2,3,4,5]
q = deque(l)

# append at the end
q.append(6)
print(q)

# append at the start
q.appendleft(0)
print(q)

# pop from right
q.pop()
print(q)

# pop from start
q.popleft()
print(q)

# extend a q at the end
q.extend([6,7,8,9])
print(q)

# extend in the left
q.extendleft([0,-1,-2,-3])
print(q)

# rotate a queue
q.rotate(2)
print(q)

# insert in between
q.insert(3,6)
print(q)
