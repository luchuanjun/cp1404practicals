name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print("My guitar: " + name + ", first made in " + str(year))
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print(f"My {name} was first made in {year} (that's right, {year}!)")
print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# TODO 1: Format output "1922 Gibson L-5 CES for about $16,036!"
print(f"{year} {name} for about ${cost:,.0f}!")

# TODO 2: Powers of 2 right aligned
for exponent in range(10 + 1):
    power = 2 ** exponent
    print(f"2 ^{exponent:2} is {power:5}")
