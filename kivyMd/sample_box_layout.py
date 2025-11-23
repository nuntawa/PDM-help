from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget  # <-- required

Window.size = (1366,768)

class App(MDApp):
    
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_pallette = "Orange"
        self.title = "PDM Help"

        layout = BoxLayout(orientation='vertical', padding=0, spacing=0)

        label = MDLabel(
            text="KivyMD 1.2 BoxLayout Sample",
            halign="center",#"left", "center", "right", or "justify"
            font_style="H5",
            size_hint_y=.2,
            # height=50,
        )
        layout.add_widget(label)
        layout.add_widget(Widget())   # <-- pushes label to the TOP

        self.screen.add_widget(layout)

        return self.screen


if __name__ == "__main__":
    App().run()