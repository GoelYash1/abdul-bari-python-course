from collections import Counter
import re

s1 = """
    Python is an easy programming language.
    Python syntax is like the English language.
    Python language is easy to learn and adapt to compared to Java and C.
    In Python language, the same task can be performed using fewer lines of code.
    Its easy learning and easy to code.
"""

words = re.findall('\w+',s1)

count = Counter(words)

print(count.most_common(3))