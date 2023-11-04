"""
Uses a list to store all the user's guitars and
keeps inputting until they enter a blank name then print their details
"""

import csv

from guitar import Guitar


def main():
    """Continuously get inputs, to add more guitars, until user enters "". Then format print all.
    Could have included exception handling and function but wasn't asked for."""

    guitars = []
    in_file = open('guitars.csv', 'r')  # File format is like: Name,Year,Cost

    for line in in_file:
        parts = line.strip().split(',')  # Strip newline from end and split it into parts (CSV)
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))  # Construct a Guitar object using the elements
        guitars.append(guitar)  # Add the guitar we've just constructed to the list
    in_file.close()  # Close the file as soon as we've finished reading it

    # ALTERNATIVE METHOD:
    # with open('guitars.csv', 'r') as in_file:
    #     reader = csv.reader(in_file)
    #     for row in reader:
    #         name, year, cost = row
    #         guitar = Guitar(name, int(year), float(cost))
    #         guitars.append(guitar)

    # Sort the list of guitars based on the year attribute (Needs the __lt__ class method to work)
    sorted_guitars = sorted(guitars)
    # Loop through and display all sorted guitars (using their str method)
    for guitar in sorted_guitars:
        print(guitar)

    # print("My guitars!")
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     for item in [[name, year, cost]]:
    #         print(f"{item[0]} ({item[1]}) : $({item[2]:.2f}) added.")
    #
    # # FOR TESTING:
    # # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    #
    # print("These are my guitars: ")
    # for i, guitar in enumerate(guitars, 1):
    #     vintage_string = "(vintage)" if guitar.is_vintage() else ""
    #     print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


if __name__ == '__main__':
    main()
