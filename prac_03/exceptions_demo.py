"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - When the user inputs a non-integer value (e.g., a letter) instead of a number.
2. When will a ZeroDivisionError occur?
   - When the user inputs zero as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by checking if denominator is zero before division, or using try-except.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(f"Result: {fraction}")
except ValueError:
    print("Numerator and denominator must be valid numbers!")



print("Finished.")
