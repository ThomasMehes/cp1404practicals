"""
CP1404 Practical
Program asks the user how many "quick picks" they wish to generate. Then it generates
that many lines of output. Each line consists of 6 random numbers between 1 and 45 (no repeats)
"""

import random

# Define constants
MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

def main():
    """Generate and display quick picks"""
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        number_of_picks = int(input("Please enter an positive integer: "))
    for i in range(number_of_picks):
        quick_picks = generate_quick_pick()
        print(" ".join(map(str, quick_picks)))  # map applies .join each item in the iterable to avoid explicit loops


def generate_quick_pick():
    """Function to generate a single quick pick"""
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    return sorted(quick_pick)  # ensures ascending order


main()
