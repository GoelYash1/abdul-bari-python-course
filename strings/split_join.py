s = 'a-b-c-d-e'

# replace will replace all (if not mentioned) the occurrence of a substring to a substring you want
print(s.replace("-",",",3))
print(s.replace("-",","))

# join will make a join of two strings
s1 = "xyz"
s2 = "abc"
print(s1.join(s2)) #axyzbxyzc (taking a char from s2 then whole s1 and so on till the second last char in s2)

# split will split a string based on a separator (to a mutable list)
s3="john smith ajay"
print(s3.split()) # by default the separator is white space or any space

s3="john,smith,ajay"
print(s3.split(","))
print(s3.split(",",1))

# rsplit is used to split from the right
print(s3.rsplit(",",1))

# splitlines
s4 = "aaa\nbbb\tccc\rddd\feee"
print(s4.splitlines())
print(s4.splitlines(keepends=True))
print(s4.split())

