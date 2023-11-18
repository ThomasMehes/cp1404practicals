"""
Write a taxi simulator program that uses the Taxi and SilverServiceTaxi classes.
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Each time, until they quit: user can choose a taxi and drive a desired distance.
    At the end of each trip, the trip cost is displayed and add it to their total bill."""
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
            total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(MENU)
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi):
    """user can choose how far they want to drive and handles not choosing a taxi first."""
    if current_taxi:
        current_taxi.start_fare()
        distance_selection = float(input("How far to Drive (Km)? "))
        current_taxi.drive(distance_selection)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    else:
        print("Choose a taxi before you can drive")
        trip_cost = 0
    return trip_cost  # ignore


def choose_taxi(current_taxi, taxis):
    """User chooses from a list of available taxis, until an appropriate decision is made"""
    valid_input = False
    while not valid_input:  # Used a while loop because I didn't like the examples exiting approach.
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
    """Displays each of the taxi option from the list with numbering from 0."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
