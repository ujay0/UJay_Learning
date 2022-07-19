# a=true		#NameError: name 'true' is not defined
b = True
print(type(b))
print(b)

x = 10
y = 20
z = x > y
print(type(z))
print(z)

# Internally
# True = 1
# False = 0
print(True + True)
print(True - False)
print(True * False)
# print(True/False)	#ZeroDivisionError: division by zero
