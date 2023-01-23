from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi(100, "Prius"), SilverServiceTaxi(100, "Limo", 2), SilverServiceTaxi(200, "Hummer", 4)]
    current_taxi = None
    bill = 0

    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available")
            display_taxi_option(taxis)
            current_taxi = get_valid_taxi_number(taxis)
        elif user_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = int(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to data: ${bill:.2f}")
        user_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxi_option(taxis)


def display_taxi_option(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi_number(taxis):
    try:
        taxi_number = int(input("Choose taxi: "))
        chosen_taxi = taxis[taxi_number]
        return chosen_taxi
    except IndexError:
        print("Invalid taxi choice")



main()