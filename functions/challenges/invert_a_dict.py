def invert(d):
    invert_dict = {}
    if type(d) == dict:
        for k,v in d.items():
            invert_dict[v] = k
    return invert_dict

d1 = {'a':10,'b':20,'c':30,'d':40}
d2 = invert(d1)

print(d2)