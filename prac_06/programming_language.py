"""CP1404 Practical - simple class for a programming languages"""


class ProgrammingLanguage:
    """simple class for a programming languages"""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string formatting"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Return a string representation of the object."""
        return str(self)

    def is_dynamic(self):
        """Returns True if the programming language is dynamically typed, False otherwise"""
        return self.typing.lower() == "dynamic"
