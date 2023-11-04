"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print("----------" * 13)  # simply add a line between data and words
    print_data(data)

    subject_to_data = convert_data(data)
    print(subject_to_data)
    subject = input("What subject code: ")
    print(f"{subject_to_data[subject[0]]} teaches {subject}")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        data.append(parts)  # add each formatted list into a larger list
        # print("----------")
    input_file.close()
    return data


def print_data(data):
    """print data as formatted string in plain english"""
    for i in data:
        print(f"{i[0]} is taught by {i[1]} and has {i[2]} students")


def convert_data(data):
    "turns list into dictionary so parts can be searched not individually compared"
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]
    return subject_to_data


main()
