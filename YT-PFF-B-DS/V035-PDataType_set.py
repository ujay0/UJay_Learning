s = {10, 'durga', 20, 10, 30, 40}
print('Type s:', type(s))
print('SET s:', s)

# print('Set element s[0]',s[0])		#TypeError: 'set' object is not subscriptable
# print('Set slicing s[1:4]',s[1:4])		#TypeError: 'set' object is not subscriptable
s.add(50)  # We cannot use append as we cannot insure the location/order where object vaue is going to be added
print('SET s after addition:', s)
s.remove(30)
print('SET s after removal:', s)

# Used to store Group of Values as a Single entity, where Duplicates are not allowed & order is not preserved Set Data Type.
# Thus proving Set is Growable in nature
# Thus proving Set is Mutable in nature
