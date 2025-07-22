from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class MilesConverterApp(App):
    km_result = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.km_result = "0.0"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        self.km_result = self.convert(self.root.ids.input_miles.text)

    def handle_increment(self, change):
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0.0
        value += change
        self.root.ids.input_miles.text = str(value)
        self.km_result = self.convert(str(value))

    def convert(self, miles_text):
        try:
            miles = float(miles_text)
            km = miles * CONVERSION_FACTOR
            return f"{km:.3f}"
        except ValueError:
            return "0.0"
