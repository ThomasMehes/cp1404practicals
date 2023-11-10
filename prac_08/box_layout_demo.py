from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """App lets user enter and clear their name, and greets them when we press greet button"""
    def build(self):
        """Basic setup of kivy app"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Reads text input and prints string to label"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears both label and text input"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
