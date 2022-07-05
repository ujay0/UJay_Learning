x=10+20j
print(type(x))
print(x)
x=10.5+20.6J
print(type(x))
print(x)
print("REAL:::",x.real)
print("IMAGINARY:::",x.imag)

#x=10+20i	#SyntaxError: invalid syntax
#x=10+j20	#NameError: name 'j20' is not defined
#print(type(x))
#print(x)