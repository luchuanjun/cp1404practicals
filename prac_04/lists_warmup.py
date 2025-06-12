numbers = [3, 1, 4, 1, 5, 9, 2]

# Answers without running the code:
# numbers[0] => 3
# numbers[-1] => 2
# numbers[3] => 1
# numbers[:-1] => [3, 1, 4, 1, 5, 9]
# numbers[3:4] => [1]
# 5 in numbers => True
# 7 in numbers => False
# "3" in numbers => False (because "3" is a string, numbers contains ints)
# numbers + [6, 5, 3] => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#Changing elements
numbers[0] = "ten"  # Change first element to string "ten"
numbers[-1] = 1     # Change last element to 1

#Printing elements except the first two
print(numbers[2:])

 # Print whether 9 is in numbers
print(9 in numbers)
