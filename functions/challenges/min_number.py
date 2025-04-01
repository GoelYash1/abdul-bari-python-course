def minimum(*args,low_limit=None):
    if low_limit is None:
        return min(args)
    else:
        l2 = [x for x in args if x>low_limit]
        return min(l2)

l1 = (1,2,-10,3,-5)
print(minimum(*l1))
print(minimum(*l1,low_limit=0))