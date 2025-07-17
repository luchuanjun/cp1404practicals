from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    def build(self):
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        try:
            value = float(self.root.ids.input_number.text)
            result = value ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


if __name__ == '__main__':
    SquaringApp().run()
