from prac_09.car import Car
import random


class UnreliableCar(Car):
    """A car that sometimes fails to drive the full requested distance."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance.

        :param name: name of the car
        :param fuel: initial amount of fuel
        :param reliability: float between 0 and 1 indicating probability the car drives successfully
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car a given distance if it is reliable enough.

        The car only drives if a random number between 0 and 1 is less than the reliability.
        Otherwise, it drives 0 km (it breaks down).

        :param distance: intended distance to drive
        :return: actual distance driven
        """
        if random.random() < self.reliability:
            # Drive normally (up to fuel limit)
            return super().drive(distance)
        else:
            # Car breaks down, drives 0 km
            print(f"{self.name} is unreliable and broke down!")
            return 0
