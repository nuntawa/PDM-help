from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar


Window.size = (1366,768)



class App(MDApp):
    
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_pallette = "Orange"
        self.title = "PDM Help"

        toolbar  = MDTopAppBar(
            title="PDM Help",
            pos_hint={"top": 1},
            left_action_items=[["menu", lambda x: self.menuClick()]],
        )
       
        self.screen.add_widget(toolbar)
        return self.screen

    def menuClick(self):
        print("menuClick")

if __name__ == "__main__":
    App().run()