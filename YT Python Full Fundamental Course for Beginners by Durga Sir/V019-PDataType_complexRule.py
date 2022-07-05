x=10+20j
print(type(x))
print(x)
x=10.5+20.6J
print(type(x))
print(x)
print("REAL:::",x.real)
print("IMAGINARY:::",x.imag)
x=0b1111+20.6J
print(type(x))
print(x)
print("REAL:::",x.real)
print("IMAGINARY:::",x.imag)

#x=0b1111+0b1111J  #SyntaxError: invalid syntax


y=20+30J
print("SUM",x+y)
print("MULTIPLICATION",x*y)
print("DIVISION",x/y)