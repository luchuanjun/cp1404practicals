from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness factor and flagfall."""

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.flagfall = 4.5

    def get_fare(self):
        """Return the price for the taxi trip, including fanciness multiplier and flagfall."""
        base_fare = super().get_fare()
        return self.flagfall + base_fare * self.fanciness

    def __str__(self):
        """Return a string like Taxi but with flagfall and fanciness."""
        return (f"{super().__str__()}, flagfall=${self.flagfall:.2f}, "
                f"fanciness x{self.fanciness}")


if __name__ == "__main__":
    taxi = SilverServiceTaxi("FancyTaxi", 100, 1.23, 2)
    taxi.start_fare()
    taxi.drive(18)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")
