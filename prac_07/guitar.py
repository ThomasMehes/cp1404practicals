"""CP1404 Practical - ...."""


class Guitar:
    """"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise ..... """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string formatting. Example: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return a string representation of the object."""
        return str(self)

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Returns how old the guitar is in years"""
        age = 2023 - self.year
        return age

    def is_vintage(self):
        """Returns True if guitar is 50 years or older, otherwise False"""
        return self.get_age() >= 50
