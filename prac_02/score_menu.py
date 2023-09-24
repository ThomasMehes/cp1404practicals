"""
Python program following the standard menu pattern structure.
Gets user input and evaluates them as a grade or converts into stars(*).
"""


def main():
    """Get user input in menu and completes relevant tasks, see each individual function"""
    score = 0  # initial value so it option 'G' isn't chosen first the program doesn't break

    MENU = """
    G - Get a valid score (0-100)
    P - Print result
    S - Show stars
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            get_valid_score(score)
        elif choice == "P":
            result = score_category(score)
            print(f"{result}")
        elif choice == "S":
            star_converter(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def get_valid_score(score):
    """Makes sure user input score is within the bounds 0-100 inclusive, if not it continues to asks the user again"""
    while score < 0 or score > 100:
        print("Invalid input, must be between 0 to 100 inclusive")
        score = float(input("Enter score: "))


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


def star_converter(score):
    """turns score into string of stars the length of the integer"""
    print(score * "*")


main()
