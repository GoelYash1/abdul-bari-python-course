s = "python is very easy"

# startswith tells us if a string (case-sensitive) starts with a particular string (True/False)
print(s.startswith("py"))
print(s.startswith("Py"))
print(s.startswith("is",7))
print(s.startswith("is",7,8)) # end - start should be >= length of string asked

# endswith tells us if a string ends with a particular substring
print(s.endswith("easy"))
print(s.endswith("is",7,9))

# removeprefix is used to removeprefix
print(s.removeprefix("py"))
print(s.removeprefix("Py")) # If there is no prefix like that then nothing will be removed

# removesuffix is used to removesuffix
print(s.removesuffix("easy"))
print(s.removesuffix("syy")) # If there is no suffix like that then nothing will be removed

# partition is used to divide a string into different string tuple
print(s.partition("is"), type(s.partition("is")))

# rpartition is used to divide a string from the right into a tuple of three
print(s.rpartition("s"))