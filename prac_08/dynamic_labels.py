"""
CP1404
Very simple app that has a list of names (strings) and dynamically creates a separate Label for each one.
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple app that dynamically create labels based on content of dictionary"""

    def __init__(self, **kwargs):
        """Construct main app and dictionary"""
        super().__init__(**kwargs)
        self.number_to_name = {"1": "Bob Brown", "2": "Cat Cyan", "3": "Oren Ochre", "4": "Billy Bean"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """create a label for each data entry and add to the "main" layout widget"""
        for number, name in self.number_to_name.items():
            temp_label = Label(text=f'{name}')
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
