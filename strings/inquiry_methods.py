s = "HELLO"
# istitle, isupper, islower checks exactly what you expect
print(f"Is {s} a upper string = {s.isupper()}")
print(f"Is {s} a lower string = {s.islower()}")
print(f"Is {s} a title string = {s.istitle()}")

# For empty strings it gives false
print("For empty string, islower, isupper, istitle all give False")
print("".isupper())
print("".islower())
print("".istitle())

# For string with alphabet and/or numbers only, we use isalnum to check
s = 'abc123'
print(f"Is {s} a alpha numeric string: {s.isalnum()}")
s = 'abc-123'
print(f"Is {s} a alpha numeric string: {s.isalnum()}")

# If all are ascii characters, then isascii can be used
print(f"Is {s} a ascii string: {s.isascii()}")

# If all characters are space then isspace will return true
print(f"Is '    ' a spaced string = {"   ".isspace()}")
print(f"Is '' a spaced string = {"".isspace()}")
print(f"Is 'a ' a spaced string = {"a ".isspace()}")

