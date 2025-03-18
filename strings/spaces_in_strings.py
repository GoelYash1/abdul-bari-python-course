s1="python"
print(s1.ljust(10, "*"))
print(s1.rjust(10,"*"))
print(s1.center(10,"*"))

# Removing characters or spaces
s2 = "   python   "
print(s2.lstrip(), len(s2.lstrip()))
print(s2.rstrip(), len(s2.rstrip()))
print(s2.strip(), len(s2.strip()))

s3 = "... ... ++aaapython"
print(s3.lstrip("."))
print(s3.lstrip(". +"))
print(s3.lstrip(". +a"))
