def main():
    """Main function to run the score menu program."""
    score = get_valid_score()  # Get a valid score before starting the menu loop

    menu = "\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Score result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell. Thank you for using the score menu!")


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive."""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = float(input("Enter a valid score (0-100): "))
    return score


def get_score_result(score):
    """Determine the result for the given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars equal to the integer value of the score."""
    print("*" * int(score))

# Program entry point
if __name__ == "__main__":
    main()
