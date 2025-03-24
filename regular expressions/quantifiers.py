from re import *

print(match('a', 'a').group())
print(match('a|b', 'a').group())
print(match('a|b', 'b').group())
print(match('abc', 'abc').group())
print(match('abc', 'abcd').group())
print(match('[abc]', 'abcd').group())
print(match('[abc]', 'bcd').group())
print(match('[abc]+', 'bcd').group())
print(match('[abc]+', 'cccccc').group())
print(match('[abc]{5}', 'ababcbcaaab').group())
print(match('[a-z]+', 'ababcbcaaab').group())
print(match('[a-zA-Z0-9]+', 'abXWEDGRGFED213234abcbcaaab').group())

x = r'^Hell'
c = compile(x)
r = c.search('Hello World')
print(r.group())

x = r'rld$'
c = compile(x)
r = c.search('Hello World')
print(r.group())