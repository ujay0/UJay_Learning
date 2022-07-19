x = 10
y = x
print(id(x))
print(id(y))
y = y + 1

print(x)
print(id(x))
print(y)
print(id(y))
