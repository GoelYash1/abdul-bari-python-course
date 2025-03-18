s = "length1"

# If the given string a valid variable name then isidentifier will print true
print(f"Is {s} a valid variable name: {s.isidentifier()}")

s="1length"
print(f"Is {s} a valid variable name: {s.isidentifier()}")

# If any char like \n, \t etc. is there then isprintable will return False else True
s = "hello"
print(f"Is {s} printable: {s.isprintable()}")
s = "hello\nhello"
print(f"Is {s} printable: {s.isprintable()}")

# If a string is a natural number without superscripts (in any language), isdecimal print True
s = "125"
print(f"Is {s} a natural number without superscripts: {s.isdecimal()}")

s="1.25"
print(f"Is {s} a natural number without superscripts: {s.isdecimal()}")

# If a string only has digits whether it be in any super or under script etc.
s="8\u00b2"
print(f"Is {s} a natural number without superscripts: {s.isdecimal()}")
print(f"Is {s} a number with only digits: {s.isdigit()}")
