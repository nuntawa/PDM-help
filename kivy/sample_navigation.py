# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder

# Define screens in Python
class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

# Define the ScreenManager
class WindowManager(ScreenManager):
    pass

# Load the KV design string
kv = """
WindowManager:
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the First Screen'
        Button:
            text: 'Go to Second Screen'
            on_release: app.root.current = 'second'
            # Optional transition control:
            # on_release: app.root.transition.direction = 'left'; app.root.current = 'second'

<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Second Screen'
        Button:
            text: 'Go Back'
            on_release: app.root.current = 'first'
            # Optional transition control:
            # on_release: app.root.transition.direction = 'right'; app.root.current = 'first'
"""

class NavigationApp(App):
    def build(self):
        self.screen_manager = Builder.load_string(kv)
        # Set default transition for the manager (optional)
        self.screen_manager.transition = SlideTransition(duration=.4)
        return self.screen_manager

if __name__ == '__main__':
    NavigationApp().run()
