from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.list import MDList,OneLineListItem

Window.size = (1366, 768)

class SecondScreen():

    def __init__(self ):
        self.screen_second = Screen(name="second")

    def renderScreen(self):
        return self.screen_second

class App(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        root = MDNavigationLayout()
        self.title = "PDM Help"

        # Drawer
        self.drawer = MDNavigationDrawer()
        self.drawer.radius = (0, 0, 0, 0)
        list_view = MDList(pos_hint={"top":1}, size_hint=(1, 1))

        item1 = OneLineListItem(text="item1",on_release=lambda x : self.change_screen('main') )
        item2 = OneLineListItem(text="item2",on_release=lambda x : self.change_screen('second') )

        list_view.add_widget(item1)
        list_view.add_widget(item2)

        self.drawer.add_widget(list_view)


        # Toolbar + content container
        layout = BoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="PDM Help       ",
            left_action_items=[["menu", lambda x: self.drawer.set_state("toggle")]],
            elevation=0,
            anchor_title="center"
        )

        layout.add_widget(toolbar)

        # Main content
        content = MDLabel(
            text="Main screen content here...",
            halign="center",
            pos_hint={"center_y": 0.5},
        )
        layout.add_widget(content)

        screen = Screen(name="main")#ต้องกำหนด name ใฟ้กับ Screen
        screen.add_widget(layout)

        #screen_second = Screen(name="second")#ย้ายไปอยู่ใน  class

        # ScreenManager
        self.sm = ScreenManager()
        self.sm.add_widget(screen)
        self.sm.add_widget(SecondScreen().renderScreen())

        # Add to root
        root.add_widget(self.sm)
        root.add_widget(self.drawer)

        return root

    def change_screen(self, screen_name):
        self.sm.current = screen_name
        self.drawer.set_state("close")

App().run()
