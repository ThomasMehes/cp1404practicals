"""
CP1404 - Week 3 Practical
demonstrating the different uses of the random function including:
.randint .randrange & .uniform
"""


import random

print(random.randint(5, 20))  # line 1
# any integer from 5 to 20 (inclusive)
# the smallest number: 5
# the largest number: 20

print(random.randrange(3, 10, 2))  # line 2
# all odd numbers from 3 to 10
# the smallest number: 3
# the largest number: 9
# you would never see the number 4

print(random.uniform(2.5, 5.5))  # line 3
# any floating point number from 2.5 to 5.5
# the smallest number: 2.5
# the largest number: 5.5 (could be 5.499999etc but depends on rounding as stated when hovering over inputs)

print(random.uniform(1, 100))
# any number from 1 to 100 inclusive
