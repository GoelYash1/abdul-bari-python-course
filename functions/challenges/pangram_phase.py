import string

def pangram(s=""):
    st = set(string.ascii_lowercase)
    for c in s.lower():
        if c in st:
            st.remove(c)
    return len(st) == 0

s1 = 'the quick brown fox jumps over the lazy dog'
s2 = 'My name is Yash Goel'

s1_pangram = pangram(s1)
s2_pangram = pangram(s2)

print(f"Is '{s1}' a pangram string: ",s1_pangram)
print(f"Is '{s2}' a pangram string: ",s2_pangram)