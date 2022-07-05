a=15
b=0b10
c=0o567
d=0XBeEF

print(type(a))
print("A =",a)
print("Binary",bin(a))
print("Octal",oct(a))
print("Hexa",hex(a))


print(type(b))
print("B =",b)
print("Binary",bin(b))
print("Octal",oct(b))
print("Hexa",hex(b))

print(type(c))
print("C =",c)
print("Octal",oct(c))
print("Binary",bin(c))
print("Hexa",hex(c))

print(type(d))
print("D =",d)
print("Hexa",hex(d))
print("Binary",bin(d))
print("Octal",oct(d))

#d=0XBEEr #SyntaxError: invalid syntax
#print(type(d))
#print(d)