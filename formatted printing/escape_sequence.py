# \n is used to enter
print("abc\ndefghi") # Output: abc
                            #  defghi

# \r is used to overwrite
print("abc\rdefghi") # Output: defghi

# \f is used to enter at the same column
print("abc\fdefghi") # Output: abc
                            #     defghi

# \b is backspace and can be used to delete the last alphabet
print("abc\bdefghi") # Output: abdefghi

# \t is tab whitespace
print("abc\tdefghi") #Output: abc   defghi

# \' or \" can be used to print ' or " only
print("a\"a")
print('a\'a')

# \\ can be used for backslash i.e \
print("a\\a")

# dollar sign, rupees sign, yen sign, pound sign, copyright sign and much more with \N{'something here'}
print("\N{dollar sign}")
print("\N{yen sign}")
print("\N{superscript five}")

