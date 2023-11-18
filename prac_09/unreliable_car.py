"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that reliability %."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, reliability={self.reliability}%"

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            return f"Car broke down."
        return f"Car drove a distance of: {distance_driven} km"
