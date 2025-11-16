from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (1000, 700)


 

class DemoApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.title = "PDM Help" 
        screen = Screen()
        label = MDLabel(text='Hello world',
                        halign='center',
                        theme_text_color="Primary",#Error #secondary
                        font_style='H2'#Caption
                )
        screen.add_widget(label)
        return screen
    

if __name__ == "__main__":
    DemoApp().run()