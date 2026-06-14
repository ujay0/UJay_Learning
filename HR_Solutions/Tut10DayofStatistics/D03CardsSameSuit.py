# !/bin/python3

# Task
# A standard deck of 52 playing cards has 4 suits (hearts, diamonds,
# clubs, and spades) and 13 ranks (2 through 10, Jack, Queen, King, and Ace).
# What is the probability of drawing 2 cards from the deck such that all 2 cards
# are of the same suit?


# Total ways to choose 2 cards from 52
import math
from itertools import combinations, product
from fractions import Fraction


# total_ways = math.comb(52, 2)
# # Ways to choose 2 cards from the same suit
# same_suit_ways = 4 * math.comb(13, 2)
# # Probability of drawing 2 cards of the same suit
# probability = Fraction(same_suit_ways, total_ways)
# print("The probability of drawing 2 cards of the same suit is:", probability)


suits = ['spades', 'hearts', 'clubs', 'diamonds']

card_values = ['2','3','4','5','6','7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# create all possible cards
deck = list(product(suits, card_values))

# all possible two card drawing combinations
two_cards_drawn = list(combinations(deck,2))

number_two_card_combinations = len(two_cards_drawn)

# initialise our target
wished_event = 0

for i in range(number_two_card_combinations):

    # when both suits (first part of the tuple (suit, value)) are the same
    if two_cards_drawn[i][0][0] == two_cards_drawn[i][1][0]:
        wished_event += 1

# get the fraction of our wished event from all combinations
print(Fraction(wished_event/number_two_card_combinations).limit_denominator()) # evaluates to 4/17