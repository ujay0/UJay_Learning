#!/bin/python3



# Task
# There are 3 urns labeled X, Y, and Z.


# Urn X contains 4 red balls and 3 black balls.
# Urn Y contains 5 red balls and 4 black balls.
# Urn Z contains 1 red ball and 1 black ball.

# One ball is drawn from each of the  urns. What is the probability that, of the  balls drawn,  are red and  is black?
# Probabilities
urn_x = {'R': 4/7, 'B': 3/7}
urn_y = {'R': 5/9, 'B': 4/9}
urn_z = {'R': 1/2, 'B': 1/2}

# Scenarios
scenarios = [
    ['R', 'B', 'R'],  # R from X, B from Y, R from Z
    ['B', 'R', 'R'],  # B from X, R from Y, R from Z
    ['R', 'R', 'B']   # R from X, R from Y, B from Z
]

# Calculate probabilities for each scenario
total_probability = 0
for scenario in scenarios:
    probability = 1
    for i in range(3):
        if i == 0:
            probability *= urn_x[scenario[i]]
        elif i == 1:
            probability *= urn_y[scenario[i]]
        else:
            probability *= urn_z[scenario[i]]
    total_probability += probability
		
print("The probability of drawing 2 red balls and 1 black ball is:", total_probability)