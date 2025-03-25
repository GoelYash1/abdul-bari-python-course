from re import *

print("'a' match 'a'",match('a', 'a').group())
print("a|b match 'ab",match('a|b', 'ab').group())
print("a|b match 'ba'", match('a|b', 'ba').group())
print("'abc' match 'abc'",match('abc', 'abc').group())
print("'abc' match 'abcd'",match('abc', 'abcd').group())
print("'[abc]' match 'abcd'",match('[abc]', 'abcd').group())
print("'[abc]' match 'bcd'",match('[abc]', 'bcd').group())
print("'[abc]+' match 'bcd'",match('[abc]+', 'bcd').group())
print("'[abc]+' match 'cccccc'",match('[abc]+', 'cccccc').group())
print("'[abc]{5}' match 'ababcbcaaab'",match('[abc]{5}', 'ababcbcaaab').group())
print("'[a-z]+' match 'ababcbcaaab'",match('[a-z]+', 'ababcbcaaab').group())
print("'[a-zA-Z0-9]+' match 'abXWEDGRGFED213234abcbcaaab'",match('[a-zA-Z0-9]+', 'abXWEDGRGFED213234abcbcaaab').group())

x = r'^Hell'
c = compile(x)
r = c.search('Hello World')
print(r.group())

x = r'rld$'
c = compile(x)
r = c.search('Hello World')
print(r.group())