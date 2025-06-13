import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    """Generate a single quick pick of 6 unique random numbers between MIN_NUMBER and MAX_NUMBER."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

def main():
    """Main program to generate multiple quick picks."""
    while True:
        try:
            how_many = int(input("How many quick picks? "))
            if how_many < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input; please enter a valid integer.")

    for _ in range(how_many):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

if __name__ == "__main__":
    main()
