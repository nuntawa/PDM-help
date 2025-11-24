from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer

Window.size = (1366, 768)


class App(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        root = MDNavigationLayout()
        self.title = "PDM Help"

        # Drawer
        drawer = MDNavigationDrawer()
        box = BoxLayout(orientation="vertical", padding=20, spacing=20)
        box.add_widget(MDLabel(text="Menu Item 1"))
        box.add_widget(MDLabel(text="Menu Item 2"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 3"))
        box.add_widget(MDLabel(text="Menu Item 9"))
        drawer.radius = (0, 0, 0, 0)
        drawer.add_widget(box)

        # Toolbar + content container
        layout = BoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="PDM Help",
            left_action_items=[["menu", lambda x: drawer.set_state("toggle")]],
            elevation=0,
        )

        layout.add_widget(toolbar)

        # Main content
        content = MDLabel(
            text="Main screen content here...",
            halign="center",
            pos_hint={"center_y": 0.5},
        )
        layout.add_widget(content)

        screen = Screen(name="main")
        screen.add_widget(layout)

        # ScreenManager
        sm = ScreenManager()
        sm.add_widget(screen)

        # Add to root
        root.add_widget(sm)
        root.add_widget(drawer)

        return root


App().run()
