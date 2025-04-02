# SEEK seek(offset, from) from values are 0,1,2
# 0 to read from start
# 1 to read from the current position
# 2 to read from the end

# TELL f.tell() gives the index of the pointer for file
with open('my.data','rb') as f:
    # abcdefghij
    # i
    print(f.read(2).decode())
    # abcdefghij
    #   i

    # From the current pos
    f.seek(3,1)
    # abcdefghij
    #      i

    print(f.read(1).decode())
    # abcdefghij
    #       i

    # From end of the file
    f.seek(-5,2)
    # abcdefghij
    #      i
    print(f.read().decode())
