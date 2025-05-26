"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Prompt user for sales input
sales = float(input("Enter sales: $"))

# Loop until a negative sales amount is entered
while sales >= 0:
    # Determine the bonus based on sales amount
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15

    # Display the bonus
    print(f"Bonus: ${bonus:.2f}")

    # Prompt again for next input
    sales = float(input("Enter sales: $"))
