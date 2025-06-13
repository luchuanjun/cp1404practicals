names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# lowercase_full_names: list comprehension to create all full_names in lowercase
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# convert to integers
numbers = [int(num) for num in almost_numbers]
print(numbers)

# numbers greater than 9
greater_than_9 = [num for num in numbers if num > 9]
print(greater_than_9)

# last names for full names longer than 11 chars, joined by comma
long_last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_last_names)
