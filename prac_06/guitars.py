"""
Uses a list to store all the user's guitars and
keeps inputting until they enter a blank name then print their details
Estimated: 1 hour 30 minutes (this includes from the start of guitar.py)
Actual: 1 hour 8 minutes
"""
from prac_06.guitar import Guitar


def main():
    """Continuously get inputs, to add more guitars, until user enters "". Then format print all.
    Could have included exception handling and function but wasn't asked for."""
    guitars = []
    print("My guitars!")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        for item in [[name, year, cost]]:
            print(f"{item[0]} ({item[1]}) : $({item[2]:.2f}) added.")

    # FOR TESTING:
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


if __name__ == '__main__':
    main()
