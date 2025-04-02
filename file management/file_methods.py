f = open('prop.txt','r')

# These are some properties of file
print(f.name)
print(f.mode)
print(f.closed)

# These are the methods it supports
""" FOR READING """
# readline reads line by line
line1 = f.readline()
print(line1, end='')

line2 = f.readline()
print(line2, end='')

# readlines reads whole lines and gives as a list of lines
lines = f.readlines()
print(lines, type(lines))

f.close()

f2 = open('prop.txt','w')

str1 = 'python is simple\nit is easy\neverything is an object\n'
list1 = ['python is simple\n','it is easy\n','everything is an object']

f2.write(str1)
f2.writelines(list1)

f2.close()
