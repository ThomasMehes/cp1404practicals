from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to kilometres."""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        """Handle conversion, output result to label widget."""
        try:
            result = float(value) * MILES_TO_KM
            self.output_text = str(result)
        except ValueError:
            self.output_text = '0.0'

    def handle_increment(self, increment):
        """Handle the up & down button increments of +/- 1."""
        current_text = self.root.ids.input_miles.text
        if not current_text:
            current_text = '0'
        try:
            current = float(current_text)
        except ValueError:
            current = 0.0
        self.handle_conversion(current + increment)
        self.root.ids.input_miles.text = str(current + increment)


ConvertMilesKmApp().run()
