from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

# List of names:
names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Billy Bean"]


class DynamicLabelsApp(App):
    """Simple app that dynamically create labels based on content of list"""

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name in the list and add to the "main" layout widget"""
        for name in names:
            temp_label = Label(text=f'{name}')
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
