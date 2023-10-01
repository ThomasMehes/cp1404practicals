"""
CP1404 - Week 3 Practical
4 separate file read or write based tasks.
Comment out code to run a single task.
"""

# 1.
OUTPUT_FILE = "files.txt"

user_name = str(input("Enter your name: "))
out_file = open(OUTPUT_FILE, 'w')
print(f"{user_name}", file=out_file)

out_file.close()

# 2.
INPUT_FILE = "name.txt"

in_file = open(INPUT_FILE, 'r')
name = in_file.readline()
print(f"{name}")

in_file.close()

# 3.
INPUT_FILE = "numbers.txt"
sum_of_numbers = 0

in_file = open(INPUT_FILE, 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
sum_of_numbers = number_1 + number_2
print(f"{sum_of_numbers}")

in_file.close()

# 4.
FILENAME = "numbers.txt"
sum_of_numbers = 0  # same name as previous task so make sure it is commented out.
try:
    in_file = open(FILENAME, "r")  # 'r' - read, 'w' - write, 'a' - append (write to end)
    for line in in_file:
        additional_number = int(line)
        sum_of_numbers = sum_of_numbers + additional_number
    print(f"Sum of total files numbers: {sum_of_numbers}")

# try code to show how I would have use error checking
except ValueError:
    print(f"Invalid contents in {FILENAME}")
except FileNotFoundError:
    print(f"{FILENAME} not found")
else:
    in_file.close()
