from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window



Window.size = (1000, 700)
 

class DemoApp(MDApp):
    def build(self):
        self.title = "My Custom Window Title" 
        label = MDLabel(text='Hello world',halign='center')
        return label
    

if __name__ == "__main__":
    DemoApp().run()