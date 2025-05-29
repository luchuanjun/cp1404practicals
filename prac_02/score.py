import random

def main():
    score = float(input("Enter your score (0-100): "))
    result = get_score_result(score)
    print(f"Your result: {result}")

    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
