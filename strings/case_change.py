s = "hELLO deAr"

# Capitalize first letter and lower case the rest
s_capitalize = s.capitalize()
print(f"capitalize = {s_capitalize}")

# lower changes entire to lower string
s_lower = s.lower()
print(f"lower = {s_lower}")

# upper changes entire to upper string
s_upper = s.upper()
print(f"upper = {s_upper}")

# title changes every words first letter to capital
s_title = s.title()
print(f"title = {s_title}")

# swapcase switches the case upper to lower and vice versa of every character
s_swapcase = s.swapcase()
print(f"swapcase = {s_swapcase}")

# casefold is similar to lower apart from caseless characters like (sharp s) German script
s_casefold = s.casefold()
print(f"casefold = {s_casefold}")

# Digraph in strings (though it is a single letter upper and title gives different outputs)
s1 = "\u01C6"
print(s1.upper())
print(s1.title())