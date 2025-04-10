from collections import deque

customers = ['John','James','Mark','Smith']
cust_que = deque()

def walk_in(cust):
    cust_que.append(cust)

def serviced():
    return cust_que.popleft()

for cust in customers:
    walk_in(cust)

for i in range(len(cust_que)):
    print(serviced(), "leaves the shop")
