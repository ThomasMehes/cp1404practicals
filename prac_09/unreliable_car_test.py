"""
CP1404
Test program that shows the unreliable_car subclass of Car.
"Reliability" is a float between 0 and 100, that represents the percentage chance that
the drive method will actually drive the car.
"""


from prac_09.unreliable_car import UnreliableCar


def main():
    """Demo test code to show how to use taxi subclass."""
    my_unreliable_car = UnreliableCar("Toyota Echo", 100, 80.0)
    my_unreliable_car.drive(40)  # in km
    print(my_unreliable_car)
    print(my_unreliable_car.drive(40))

    my_unreliable_car.drive(100)
    print(my_unreliable_car)
    print(my_unreliable_car.drive(100))


if __name__ == '__main__':
    main()
