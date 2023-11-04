"""
CP1404 Practical
Uses a list to store all guitars from .csv file and also stores the user's guitars and
keeps inputting until they enter a blank name then writes back to .csv file..
"""

import csv

from guitar import Guitar


def main():
    """Reads .csv file, then gets inputs to add more guitars, until user enters "" and then write to .csv."""
    guitars = []

    # Read .csv and append each line to guitars list
    in_file = open('guitars.csv', 'r')  # File format is like: Name,Year,Cost
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    # Continuously get inputs, to add more guitars, until user enters "".
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added.")
        name = input("Name: ")

    # Sort the list of guitars based on the year attribute (Needs the __lt__ class method to work)
    sorted_guitars = sorted(guitars)

    # Loop through and write all sorted guitars to .csv file
    out_file = open('guitars.csv', 'w')
    for guitar in sorted_guitars:
        print(guitar.name + ',' + str(guitar.year) + ',' + str(guitar.cost), file=out_file)
    out_file.close()

    print("Guitars saved to guitars.csv")


if __name__ == '__main__':
    main()
