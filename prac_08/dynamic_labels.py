from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    name_display = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.color = NEW_COLOUR
            self.root.ids.label_box.add_widget(temp_label)



DynamicWidgetsApp().run()