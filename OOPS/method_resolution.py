class D:
    pass

class A(D):
    pass

class X(D):
    pass

class B(A):
    pass

class Y(X):
    pass

class C(B,Y):
    pass

c = C()

# Method resolution order gives us this
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.D'>, <class 'object'>]
print(C.mro())
