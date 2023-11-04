"""
CP1404 Practical
Classes for guitars.py program.
"""


class Guitar:
    """Methods including overloading operators (__lt__)."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise ..... """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string formatting. Example: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name}, {self.year}, {self.cost:,.2f}"

    def __lt__(self, other):
        """Compares the years of Guitars to be used be sorted in main()"""
        return self.year < other.year
