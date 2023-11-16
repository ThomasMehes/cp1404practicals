from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            display_taxis(taxis)
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "D":
            drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(MENU)
        print(f"Bill to date: ${total_bill}")
        choice = input(">>> ").upper()

    print("Thank you.")


def drive_taxi(current_taxi, total_bill):
    if current_taxi:
        current_taxi.start_fare()
        distance_selection = float(input("How far to Drive (Km)? "))
        current_taxi.drive(distance_selection)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("Choose a taxi before you can drive")


def choose_taxi(current_taxi, taxis):
    valid_input = False
    while not valid_input:
        try:
            taxi_selection = int(input("Choose a taxi: "))
            if 0 <= taxi_selection < len(taxis):
                current_taxi = taxis[taxi_selection]
                valid_input = True
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid input")
    print(f"You've selected: {current_taxi}")
    return current_taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
