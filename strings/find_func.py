s = 'Hello, how are you'

# Find
H_find_index = s.find("H")
how_find_index = s.find("how")

# Between two indexes
o_find_index = s.find("o",6)

# rfind
o_rfind_index = s.rfind('o',0,len(s))

# index
o_index = s.index('o')

# count
o_count = s.count('o')

print(
    "H: ",H_find_index,
    "\nhow: ", how_find_index,
    "\nfind from 6th index o: ", o_find_index,
    "\nrfind o:",o_rfind_index,
    "\nindex o: ", o_index,
    "\ncount o: ", o_count
)