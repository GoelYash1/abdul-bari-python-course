# b is used for reading binary files
b_file1 = open('../Errors.png','rb')
data = b_file1.read()

# Created Errors2 from here
cp = open('../Errors2.png','wb')
cp.write(data)

b_file1.close()
cp.close()