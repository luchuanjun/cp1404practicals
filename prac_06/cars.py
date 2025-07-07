class Car:
    def __init__(self, name, fuel=0):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        if amount > 0:
            self.fuel += amount

    def drive(self, distance):
        if distance < 0:
            print("Distance must be >= 0")
            return 0

        # Car drives as far as fuel allows
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
            self.odometer += distance
            print(f"The car drove {distance}km and ran out of fuel.")
            return distance
        else:
            self.fuel -= distance
            self.odometer += distance
            print(f"The car drove {distance}km.")
            return distance

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
