from re import search, match


def fun(n):
    if n > 0: # This is base condition
        print(n)
        fun(n-1) # This is recursive call

def fact(n):
    if n<=0:
        return 1
    return n * fact(n-1)

fun(10)
ans = fact(5)
print(ans)



