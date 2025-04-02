# Read only
file_handler = open('MyData.txt','r')
# File pointer continues ones it is opened and started reading
str1 = file_handler.read(20)
print(str1)

# Now it will start from 20th index till 52nd index
str1 = file_handler.read(33)
print(str1)

str1 = file_handler.read()
print(str1)

# Since file is a resource for the program we should close it back
file_handler.close()