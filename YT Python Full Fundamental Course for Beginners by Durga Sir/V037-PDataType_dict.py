d = {100: 'Durga', 200: 'Software', 300: 'Solutions'}
print('Type d:', type(d))
print('DICT d:', d)

d0 = {100: 'Durga', 100: 'Software', 100: 'Solutions'}
print('DICT d0:', d0)  # If Existing Key is used the old value would be replaced by new Value
#	O/P ==++==++== O/P
# DICT d0: {100: 'Solutions'}

d1 = {}
d1[100] = 'Ram'
d1[200] = 'Sita'
d1[300] = 'Ravan'
print('DICT d1:', d1)
d1[100] = 'Durga'  # If Existing Key is used the old value would be replaced by new Value
print('DICT d1:', d1)

# Used to store Group of Key-Value pairs as a Single entity, where Duplicate Keys are not allowed & order is not preserved in Dict Data Type.
# Thus proving Set is Growable in nature
# Thus proving Set is Mutable in nature
