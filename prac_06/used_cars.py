from prac_06.car import car

# Create limo car with 100 fuel
limo = Car("Limo", 100)

# Add 20 units of fuel
limo.add_fuel(20)

# Print current fuel
print(f"Fuel in limo: {limo.fuel}")

# Attempt to drive 115 km
limo.drive(115)

# Print car status
print(limo)
