# Outer can be used as decorator
def outer(f):
    def inner():
        print('*'*10)
        f()
        print('*'*10)
    return inner

# Display is modified or decorated same as display = outer(display)
@outer
def display():
    print('Welcome')

display()