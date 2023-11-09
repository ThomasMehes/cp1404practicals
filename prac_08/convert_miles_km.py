"""
CP1404 Week 8 prac - KIVY program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to kilometres."""

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
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def handle_increment(self, increment):
        """Handle the up & down button increments of +/- 1."""
        current = float(self.root.ids.input_miles.text)
        self.handle_conversion(current + increment)
        self.root.ids.input_miles.text = str(current + increment)


ConvertMilesKmApp().run()
