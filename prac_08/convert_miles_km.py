"""
CP1404 Week 8 prac - KIVY program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKmApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


ConvertMilesKmApp().run()
