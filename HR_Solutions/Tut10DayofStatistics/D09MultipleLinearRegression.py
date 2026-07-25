#!/bin/python3

# If Y is linearly dependent only on X, then we can use the ordinary least square regression 
# line, Y=a+bx . However, if Y shows linear dependency on m variables X1, X2, ..., Xm, then 
# we need to find the values of X1, X2, ..., Xm and the other constants (a and b1, b2, ..., bm ).
# We can then write the regression equation as:

    #  y = a + b1*x1 + b2*x2 + ... + bm*xm

# Matrix Form of the Regression Equation
# Let's consider that Y depends on two variables, X1 and X2. We write the regression relation
# as Y = a + b1*X1 + b2*X2. 
# Consider the following matrix operation:
    #               [a]   
    # [1 x1 x2]     [b1]   = a + b1*x1 + b2*x2
    #               [b2]
# We define two matrices, X and B:
#  x = [1 x1 x2]
#  B = [a b1 b2]^T
# Now, we rewrite the regression relation as Y = X * B. This transforms the regression relation 
# into matrix form.
