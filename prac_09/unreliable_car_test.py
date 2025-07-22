import unittest
from prac_09.unreliable_car import UnreliableCar

class TestUnreliableCar(unittest.TestCase):

    def setUp(self):
        self.car = UnreliableCar("TestCar", 100, 0.7)  # 70% reliability

    def test_drive_within_fuel(self):
        distance = 50
        driven = self.car.drive(distance)
        # driven should be either 0 or distance depending on reliability
        self.assertIn(driven, [0, distance])
        if driven > 0:
            self.assertEqual(self.car.fuel, 100 - driven)
        else:
            self.assertEqual(self.car.fuel, 100)

    def test_drive_multiple_attempts(self):
        distances = [20, 30, 40]
        total_driven = 0
        for distance in distances:
            driven = self.car.drive(distance)
            self.assertIn(driven, [0, distance])
            if driven > 0:
                total_driven += driven
        self.assertLessEqual(total_driven, 100)  # Can't drive more than fuel

if __name__ == "__main__":
    unittest.main()
