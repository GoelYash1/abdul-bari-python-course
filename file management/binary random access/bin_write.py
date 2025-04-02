# With open automatically closes it
with open('my.data', 'ab') as f:
    f.write('abcdefghij'.encode())