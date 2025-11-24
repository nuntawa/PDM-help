from kivymd.app import MDApp
from kivy.core.window import Window
# Use MDScreen and MDScreenManager for proper structure
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager 
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty

Window.size = (1366, 768)

# --- 1. Content for the Drawer (Unchanged) ---
class ContentNavigationDrawer(MDBoxLayout):
    pass # No change needed here for the error

# --- 2. Main Content Screen ---
class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # We need a reference to the NavigationLayout to control the drawer
        # This will be set later in the App's build method
        self.nav_layout = None 
        
        # Setup Toolbar
        self.toolbar = MDTopAppBar(
            title="PDM Help",
            pos_hint={"top": 1},
            # This action now calls a method to open the drawer
            left_action_items=[["menu", lambda x: self.open_nav_drawer()]],
        )
        self.add_widget(self.toolbar)
        
        # Add some main content
        self.add_widget(
            MDLabel(text="Main Screen Content", halign="center", pos_hint={"center_x": 0.5, "center_y": 0.5})
        )

    def open_nav_drawer(self):
        """Opens the navigation drawer using the stored reference."""
        if self.nav_layout:
            # We access the MDNavigationDrawer by ID from the MDNavigationLayout
            self.nav_layout.ids.nav_drawer.set_state("toggle")

# --- 3. The Main App Class ---
class App(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.title = "PDM Help"

        # A. Create the MDNavigationLayout as the root
        self.root_widget = MDNavigationLayout()
        
        # B. Create the Screen Manager (This is the fix!)
        # The MDNavigationLayout *requires* a ScreenManager for the main content area.
        self.screen_manager = MDScreenManager()

        # C. Create your Main Screen instance
        main_screen_content = MainScreen(name="main")
        
        # D. Add the Main Screen to the Screen Manager
        self.screen_manager.add_widget(main_screen_content)

        # E. Create the Navigation Drawer and its content
        nav_drawer_content = ContentNavigationDrawer(orientation="vertical", padding="8dp", spacing="8dp")
        
        # Add list items to the drawer content
        list_container = MDList()
        list_container.add_widget(OneLineListItem(text="Home", on_release=lambda x: self.menuClick("Home")))
        nav_drawer_content.add_widget(list_container)

        # F. Create the MDNavigationDrawer and add the content. 
        # Crucially, give it an ID so the toolbar can reference it.
        self.nav_drawer = MDNavigationDrawer(id="nav_drawer")
        self.nav_drawer.add_widget(nav_drawer_content)
        
        # G. Add the two required children to the MDNavigationLayout:
        # 1. The ScreenManager (main content)
        # 2. The MDNavigationDrawer (the menu)
        self.root_widget.add_widget(self.screen_manager)
        self.root_widget.add_widget(self.nav_drawer)
        
        # H. Set the reference on the main screen so it can control the drawer
        main_screen_content.nav_layout = self.root_widget
        
        return self.root_widget

    def menuClick(self, item_name):
        print(f"{item_name} clicked")
        self.nav_drawer.set_state("close") 

if __name__ == "__main__":
    App().run()