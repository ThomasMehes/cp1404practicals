"""
CP1404
Simple program that shows the functionality for the taxi class.
"""

from prac_09.taxi import Taxi


def main():
    """Demo test code to show how to use taxi subclass."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)  # in km
    print(my_taxi)
    print(f"Current fare is accumulated to ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare is accumulated to ${my_taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
