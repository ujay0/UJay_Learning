t = (10, 'durga', 20, 10, 30)
print('Type t:', type(t))
print('Tuple t:', t)

print('Tuple t[0]:', t[0])
print('Tuple t[-1]:', t[-1])
print('Tuple t[1:4]:', t[1:4])  # Tuple Slicing from index 1 to 4 i.e (4-1) = 3 elements

# t[0]=7777		#TypeError: 'tuple' object does not support item assignment
# t.append(50)	#AttributeError: 'tuple' object has no attribute 'append'
# t.remove(10)	#AttributeError: 'tuple' object has no attribute 'remove'


# Used to store Group of Values as a Single entity, where order is Important & Duplicates are allowed but Object value cannot be changed we use Tuple Data Type.
