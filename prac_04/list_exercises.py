"""
CP1404 Practical
Basic list operations
"""
numbers = []
for i in range(5):
    number = float(input(f"Number {i+1}: "))  # though it would be helpful to display which number the user is up to
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/len(numbers)}")

