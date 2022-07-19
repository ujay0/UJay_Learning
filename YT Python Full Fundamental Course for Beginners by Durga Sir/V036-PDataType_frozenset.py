s = {10, 20, 10, 30, 40}
print('Type s:', type(s))
print('SET s:', s)

fs = frozenset(s)

print('Type fs:', type(fs))
print('FROZENSET fs:', fs)

# print('FROZENSET element fs[0]',fs[0])		# TypeError: 'frozenset' object is not subscriptable
# print('FROZENSET slicing fs[1:4]',fs[1:4])	# TypeError: 'frozenset' object is not subscriptable

# fs.add(50)		# AttributeError: 'frozenset' object has no attribute 'add'

# fs.remove(30)		# AttributeError: 'frozenset' object has no attribute 'remove'

fs1 = frozenset({10.5})
print('Type fs1:', type(fs1))
print('FROZENSET fs1:', fs1)

# Used to store Group of Values as a Single entity, where Duplicates are not allowed & order is not preserved & immutability we use Set Data Type.
# Thus proving Set is Not Growable in nature
# Thus proving Set is Not Mutable in nature
