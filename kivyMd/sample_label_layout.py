from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel

Window.size = (1366,768)


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.title = "PDM Help"

        screen = Screen()
       
        label = MDLabel(
            text="Label",
            halign="center",
            size_hint=(0.25, None), #กินกี่ % ของ parent ถ้า 1  คือ 100% ( กรณีนี้คือ 25% ตามแนวนอน แต่ไม่กำหนดแนวตั้ง )
            height=50,#fixed ความสูง
            pos_hint={"top": .8},  # <-- อยู่บนสุดจะมีค่าเป็น 1
            theme_text_color="Primary"
        )
        screen.add_widget(label)

        return screen




if __name__ == "__main__":
    App().run()