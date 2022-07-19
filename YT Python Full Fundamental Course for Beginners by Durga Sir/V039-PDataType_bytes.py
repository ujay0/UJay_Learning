l = [10, 20, 30, 40]
b = bytes(l)
print('Type b:', type(b))
for x in b:
    print('x in b:', x)

# l1=[10,20,30,40,256]
# b1 = bytes(l1)			# ValueError: bytes must be in range(0, 256)


# l1=[10,20,30,40,50]
# b1 = bytes(l1)
# b1[2]=77					# TypeError: 'bytes' object does not support item assignment
