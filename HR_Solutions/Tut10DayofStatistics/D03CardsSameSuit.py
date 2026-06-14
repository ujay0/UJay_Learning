# !/bin/python3

# Task
# A standard deck of 52 playing cards has 4 suits (hearts, diamonds,
# clubs, and spades) and 13 ranks (2 through 10, Jack, Queen, King, and Ace).
# What is the probability of drawing 2 cards from the deck such that all 2 cards
# are of the same suit?


# Total ways to choose 2 cards from 52
import math


total_ways = math.comb(52, 2)
# Ways to choose 2 cards from the same suit
same_suit_ways = 4 * math.comb(13, 2)
# Probability of drawing 2 cards of the same suit
probability = same_suit_ways / total_ways
print("The probability of drawing 2 cards of the same suit is:", probability)
