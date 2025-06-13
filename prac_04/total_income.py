def print_income_report(incomes):
    """Print a formatted income report with cumulative totals. """
    total = 0
    print("\nIncome Report\n-------------")
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))  # renamed from 'months' for clarity
    incomes = []



    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # using f-string
        incomes.append(income)

    print_income_report(incomes)

if __name__ == "__main__":
    main()
