"""
CP1404 - Practical
Program to determine score status
"""
import random

def main():
    """ask the user for their score and print the grade"""
    score = float(input("Enter score: "))
    grade = score_category(score)
    print(f"{grade}")

    random_score = random.randint(0, 100)
    print(random_score)
    random_grade = score_category(random_score)
    print(f"{random_grade}")

def score_category(score):
    """takes in the user's score as a parameter and returns the result to be printed"""
    if score < 0:
        grade = "Invalid score"
    elif score > 100:
        grade = "Invalid score"
    elif score > 90:
        grade = "Excellent"
    elif score > 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


main()
