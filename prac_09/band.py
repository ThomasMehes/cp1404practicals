
class Band:
    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to Band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument each musician is playing."""
        return '\n'.join([musician.play() for musician in self.musicians])
