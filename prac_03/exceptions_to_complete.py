"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task, see comments
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # if valid finish while loop
    except ValueError:  # error to catch non-integer values
        print("Please enter a valid integer.")
print("Valid result is:", result)
