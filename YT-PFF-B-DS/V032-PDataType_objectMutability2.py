l1 = [10, 20, 30]
l2 = l1
print('LIST l1:', l1)
print('LIST l2:', l2)
l1[0] = 7777
print('LIST l1:', l1)
print('LIST l2:', l2)
print('ID of LIST l1:', id(l1))
print('ID of LIST l2:', id(l2))

l2[1] = 8888
print('LIST l1:', l1)
print('LIST l2:', l2)

# This is Mutability Concept as the Same Object is being Updated in each assignment operation.
