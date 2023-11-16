

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to show how to use SilverServiceTaxi is a Taxi which is a Car."""
    my_fancy_taxi = SilverServiceTaxi("Bentley Coupe", 100, 2.0)
    my_fancy_taxi.drive(18)
    print(my_fancy_taxi)
    print(f"Current fare is accumulated to ${my_fancy_taxi.get_fare():.2f}")


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