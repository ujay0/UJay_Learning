r1 = range(10)
print('Type r1:',type(r1))
print('RANGE r1:',r1)
for x in r1:
	print('x value:',x)

r2 = range(1, 11)
print('Type r2:',type(r2))
print('RANGE r2:',r2)
for y in r2:
	print('Y value:',y)


# r3 = range(1, 21, 1) OR range (1,21)			# 1, 2, 3, 4, 5, 6, 7,...19, 20
# r3 = range(1, 21, 2)							# 1, 3, 5, 7, 9, 11,...17, 19
# r3 = range(1, 21, 3)							# 1, 4, 7, 10, 13, 16, 19
# r3 = range(1, 21, 4)							# 1, 5, 9, 13, 17
r3 = range(20, 1, -5)							# 20, 15, 10, 5
print('Type r3:',type(r3))
print('RANGE r3:',r3)
for z in r3:
	print('Z value:',z)

print('RANGE r2[0]:',r2[0])
print('RANGE r2[-1]:',r2[-1])
r4 = r2[1:4]
print('RANGE r2[1:4]:',r4)	#Range Slicing from index 1 to 4 i.e (4-1) = 3 elements
for i in r4:
	print ('i value in r4',i)
print('r4[1] value',r4[1])
# r4[1]=1000						# TypeError: 'range' object does not support item assignment