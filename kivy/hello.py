# import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):#inherit จาก from kivy.app import App
    def build(self):
        return Label(text="Hello World")

if __name__ == '__main__': #เพื่อเช็คว่ารันจาก จากไฟล์ไหน ( กรณีถ้าเป็นการ import  มา โดยไม่ได้รันจากไฟล์นี้ __name__ จะไม่ได้มีค่าเป็น '__main__'  )
    MyApp().run()