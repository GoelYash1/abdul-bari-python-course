# Closure functions are those functions which uses variables from outer function
def outer(msg):
    def inner():
        print('+'* 10)
        print(msg)
        print('+'* 10)
    return inner

f = outer('Python')
f()

print("\n")

def get_counter():
    count = 0
    def counter():
        nonlocal count # nonlocal is used to add to count i.e if you want to update the outside variable
        count+=1
        return count
    return counter

c1 = get_counter()
c2 = get_counter()

print(c1(), c1(), c1())
print(c2(), c2())