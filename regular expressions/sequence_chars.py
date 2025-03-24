from re import *

# \d means digits
print(match('\d+','123445').group())

# \D means non digits
print(match('\D+','envy12a').group())

# \s is checking for white-space
print(match('\s+','  ').group())

# \S is checking for non white-space
print(match('\S+','abc  ').group())

# \w is checking for alphanumeric
print(match('\w+','abc1234').group())

# \W is checking for non-alphanumeric
print(match('\W+','$#%@@sdvs').group())