import unittest
from prac_09.taxi import Taxi


class TestTaxi(unittest.TestCase):

    def setUp(self):
        self.taxi = Taxi("Prius 1", 100)  # name and fuel

    def test_str(self):
        # Initially, current_fare_distance is 0
        expected = "Prius 1, fuel=100, 0km on current fare, $1.23/km"
        self.assertEqual(str(self.taxi), expected)

    def test_start_fare_resets_distance(self):
        self.taxi.current_fare_distance = 10
        self.taxi.start_fare()
        self.assertEqual(self.taxi.current_fare_distance, 0)

    def test_drive_updates_distance(self):
        distance_driven = self.taxi.drive(20)
        self.assertEqual(distance_driven, 20)
        self.assertEqual(self.taxi.current_fare_distance, 20)

    def test_drive_with_limited_fuel(self):
        self.taxi.fuel = 5
        distance_driven = self.taxi.drive(10)  # can only drive 5
        self.assertEqual(distance_driven, 5)
        self.assertEqual(self.taxi.current_fare_distance, 5)
        self.assertEqual(self.taxi.fuel, 0)

    def test_get_fare(self):
        self.taxi.current_fare_distance = 10
        expected_fare = round(10 * Taxi.price_per_km, 1)  # should match rounding logic
        self.assertEqual(self.taxi.get_fare(), expected_fare)


if __name__ == '__main__':
    unittest.main()
