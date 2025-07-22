import unittest
from prac_09.silver_service_taxi import SilverServiceTaxi


class TestSilverServiceTaxi(unittest.TestCase):

    def setUp(self):
        self.taxi = SilverServiceTaxi("Silver", 100, 1.5, 2)

    def test_get_fare(self):
        self.taxi.start_fare()
        self.taxi.drive(10)
        expected_fare = 4.5 + (1.5 * 10 * 2)  # flagfall + distance*price*fanciness
        self.assertAlmostEqual(self.taxi.get_fare(), expected_fare)

    def test_str_contains_fanciness_and_flagfall(self):
        string = str(self.taxi)
        self.assertIn("flagfall", string)
        self.assertIn("fanciness", string)


if __name__ == '__main__':
    unittest.main()
