from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel


Window.size = (1366,768)



class App(MDApp):
    
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_pallette = "Orange"
        self.title = "PDM Help"

        layout = BoxLayout(
            orientation='horizontal',
            pos_hint={"top":1},#อยู่บนสุด
            height=70,#fixed ความสูง
            size_hint=(1, None),#ยาวเต็ม  screen
        )

        label = MDLabel(
            text="AAAAAA",
            size_hint=(.75, 1 ),# กว้าง 75% ของ parent  สูงเต็ม  parent ( เพราะ กำหนเค่าเป็น 1)
        )
        layout.add_widget(label)

        label2 = MDLabel(
            text="BBBBB",
            size_hint=(.25, 1 ),
        )
        layout.add_widget(label2)

         

        self.screen.add_widget(layout)

        return self.screen


if __name__ == "__main__":
    App().run()