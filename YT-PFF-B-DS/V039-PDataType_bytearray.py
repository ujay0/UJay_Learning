l = [10, 20, 30, 40]
ba = bytearray(l)
print('Type ba:', type(ba))  # <class 'bytearray'>

print('ba[0] value:', ba[0])
print('ba[-2] value:', ba[-2])
print('ba[1:3] value:', ba[1:3])
b0 = ba[1:3]

for x in b0:
    print('x in b0:', x)

# l1=[10,20,30,40,256]
# b1 = bytearray(l1)			# ValueError: bytes must be in range(0, 256)


l1 = [10, 20, 30, 40, 50]
b1 = bytearray(l1)
print('Type b1:', type(b1))
b1[2] = 77  # Thus proving Set is Not Mutable in nature
for x in b1:
    print('x in b1:', x)
