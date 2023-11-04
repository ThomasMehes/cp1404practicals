"""
CP1404 Practical
Basic list operations
"""
numbers = []
for i in range(5):
    number = float(input(f"Number {i+1}: "))  # though it would be helpful to display which number the user is up to
    # float was used so user could input a decimal value
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/len(numbers)}")


"""
Ask the user for their username. If the username is in the above list of authorised users,
print Access granted", otherwise print "Access denied
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_guess = str(input("Enter your username: "))
if user_guess in usernames:
    print("Access granted")
else:
    print("Access denied")
