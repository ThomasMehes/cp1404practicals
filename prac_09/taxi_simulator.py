from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
        elif choice == "D":
            print("bees")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


if __name__ == '__main__':
    main()
