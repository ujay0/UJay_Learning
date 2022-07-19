def func1():
    print('Hello')
    return None


def func2():
    return ('World')


x1 = func1()
print('Value of x1', x1)
print('Type of x1', type(x1))  # <class 'NoneType'>	
print('ID of x1', id(x1))

x2 = func2()
print('Value of x2', x2)

a = None
b = None
c = None


def f1():
    pass


d = f1()
print('Value of a,b,c,d', a, b, c, d)
print('ID of a', id(a))
print('ID of b', id(b))
print('ID of c', id(c))
print('ID of d', id(d))
