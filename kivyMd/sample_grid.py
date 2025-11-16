from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (1000, 700)

class Grid():
    def createGrid(self):
        grid = MDGridLayout(
            cols=2,           # Number of columns
            rows=3,           # (Optional) Number of rows, you can omit for automatic
            spacing=20,       # (Optional) space between widgets
            padding=20        # (Optional) padding around the grid
        )
        # Add widgets to the grid
        grid.add_widget(MDLabel(text="Cell 1", halign="center"))
        grid.add_widget(MDLabel(text="Cell 2", halign="center"))
        grid.add_widget(MDLabel(text="Cell 3", halign="center"))
        grid.add_widget(MDLabel(text="Cell 4", halign="center"))
        grid.add_widget(MDLabel(text="Cell 5", halign="center"))
        grid.add_widget(MDLabel(text="Cell 6", halign="center"))
        return grid
 

class DemoApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.title = "PDM Help" 
        screen = Screen()

        screen.add_widget(Grid().createGrid())
         
        return screen
    

if __name__ == "__main__":
    DemoApp().run()