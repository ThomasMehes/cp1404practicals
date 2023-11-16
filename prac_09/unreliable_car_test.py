

from prac_09.unreliable_car import UnreliableCar


def main():
    """Demo test code to show how to use taxi subclass."""
    my_shitbox = UnreliableCar("Toyota Echo", 100, 80.0)
    my_shitbox.drive(40)  # in km
    print(my_shitbox)
    print(my_shitbox.drive(40))

    my_shitbox.drive(100)
    print(my_shitbox)
    print(my_shitbox.drive(100))


if __name__ == '__main__':
    main()
