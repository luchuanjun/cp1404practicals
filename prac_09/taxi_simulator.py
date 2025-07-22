from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100, 1.2),
        SilverServiceTaxi("Limo", 100, 1.2, 3),
        SilverServiceTaxi("Hummer", 200, 2.5, 4),
    ]

    current_taxi = None
    total_cost = 0

    print("Let's drive!")
    while True:
        print("\nq)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
        if choice == "q":
            break
        elif choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                print(f"Selected {current_taxi.name}")
            else:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                continue
            distance = float(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            fare = current_taxi.get_fare()
            print(f"Your trip cost you ${fare:.2f}")
            total_cost += fare
        else:
            print("Invalid option")

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


if __name__ == "__main__":
    main()
