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


class App(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        root = MDNavigationLayout()
        self.title = "PDM Help"

        # Drawer
        drawer = MDNavigationDrawer()
        drawer.radius = (0, 0, 0, 0)
        list_view = MDList(pos_hint={"top":1}, size_hint=(1, 1))

        item1 = OneLineListItem(text="item1")
        item2 = OneLineListItem(text="item2")

        list_view.add_widget(item1)
        list_view.add_widget(item2)

        drawer.add_widget(list_view)

        # box = BoxLayout(orientation="vertical", padding=20, spacing=20)
        # box.add_widget(MDLabel(text="Menu Item 1"))
        # box.add_widget(MDLabel(text="Menu Item 2"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 3"))
        # box.add_widget(MDLabel(text="Menu Item 9"))
        # drawer.radius = (0, 0, 0, 0)
        # drawer.add_widget(box)

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
