dict1 = {1:2,3:4,5:6}
print("Keys: ",dict1.keys())
print("Values: ",dict1.values())
print("Items: ",dict1.items())

dict2 = {101: 'Production',102: 'Accounts',103:'Sales & Marketing',104: 'Inventory'}
dict3 = dict2.copy()

# update to update a dictionary
dict2.update({105:'Designing',106:'Packaging'})
print(dict2)

# set default is used to set default value, get value if value already there or insert a value
print(dict2.setdefault(101))
dict2.setdefault(107)
dict2.setdefault(102,"Help") # No effect as 102 is already there
dict2.setdefault(108,'Hello')
print(dict2)

l1 = [11,22,33,44]
dict4 = dict.fromkeys(l1,100)
print(dict4)

'''
    For Deleting from maps
'''
dict2[110] = 'Adv'
dict2.pop(108)
print(dict2.popitem())