"""
    This will create a new file and write
    Hello!!
    This is test..
    to it
"""
# w is used to write
file = open('ModeDemo.txt','w')
file.write("Hello!!\n")
file.write('This is a test.\n')

file.close()

"""
    This commented code will overwrite the previous text with
    Hello!
"""
# file = open('ModeDemo.txt','w')
# file.write('Hello!')
# file.close()

# 'a' appends to the previous text
file = open('ModeDemo.txt','a')
file.write('I am learning Python\n')
file.write('Do you know Python.')
file.close()

# 'r+' is used for reading and appending
file = open('ModeDemo.txt','r+')
str1 = file.read(10)
print(str1)

file.write('\nGood Bye')
file.close()

# and more are there