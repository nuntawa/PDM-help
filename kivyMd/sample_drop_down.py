from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp

Window.size = (1366, 768)


class App(MDApp):

    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.title = "PDM Help" 

        # Text field that will open the dropdown
        self.dropdown_text = MDTextField(
            hint_text="Select Item",
            readonly=True,
        )
        self.screen.add_widget(self.dropdown_text)

        # Create menu items
        menu_items = [
            {
                "text": "Option 1",
                "viewclass": "OneLineListItem",
                "height": dp(50),
                "on_release": lambda x="Option 1": self.menu_callback(x),
            },
            {
                "text": "Option 2",
                "viewclass": "OneLineListItem",
                "height": dp(50),
                "on_release": lambda x="Option 2": self.menu_callback(x),
            },
            {
                "text": "Option 3",
                "viewclass": "OneLineListItem",
                "height": dp(50),
                "on_release": lambda x="Option 3": self.menu_callback(x),
            },
        ]

        # MDDropdownMenu instance
        self.menu = MDDropdownMenu(
            caller=self.dropdown_text,
            items=menu_items,
            width_mult=3,
        )

        # Open menu when user taps inside text field
        self.dropdown_text.bind(on_touch_down=self.open_menu)

        return self.screen

    def open_menu(self, instance, value):
        if value:  # value = True when focus gained
            self.menu.open()

    def menu_callback(self, selected_text):
        # Update text field value
        self.dropdown_text.text = selected_text
        self.menu.dismiss()


if __name__ == "__main__":
    App().run()
