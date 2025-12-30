import flet as ft

def main(page: ft.Page):
    page.title = "Multi-Page Desktop App"
    page.window_width = 500
    page.window_height = 400

    def open_drawer():
        page.drawer.open = True
        page.update()

    # 🧭 Navigation: handle routing
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()  # remove all existing views

        if page.route == "/":
            page.views.append(view_home())
        elif page.route == "/settings":
            page.views.append(view_settings())
        elif page.route == "/about":
            page.views.append(view_about())

        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()  # go back
        page.update()

    # 🏠 Home Page
    def view_home():
        return ft.View(
            "/",
            [
                
               
                ft.Text("Welcome to the home page!", size=20),
                ft.ElevatedButton("Go to Settings", on_click=lambda _: page.go("/settings")),
                ft.ElevatedButton("About", on_click=lambda _: page.go("/about")),
            ],
        )

    # ⚙️ Settings Page
    def view_settings():
        return ft.View(
            "/settings",
            [
                
                # ft.AppBar(title=ft.Text("⚙️ Settings")),
                ft.Text("This is the settings page.", size=18),
                ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
            ],
        )

    # ℹ️ About Page
    def view_about():
        return ft.View(
            "/about",
            [
                
                # ft.AppBar(title=ft.Text("ℹ️ About")),
                ft.Text("Multi-page Flet desktop app example.", size=18),
                ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/")),
            ],
        )


    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.ListTile(title=ft.Text("Home"), on_click=lambda e: page.go("/")),
            ft.ListTile(title=ft.Text("Settings"), on_click=lambda e: page.go("/settings")),
            ft.ListTile(title=ft.Text("About"), on_click=lambda e: page.go("/about")),
        ],
    )
    # page.add(page.drawer)
    page.AppBar = ft.AppBar(title=ft.Text("🏠 Home Page") , bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,leading=ft.IconButton(
                    icon=ft.Icons.MENU,
                    on_click=lambda e: open_drawer()
                ), ),

    # Bind routing handlers
    # page.on_route_change = route_change
    # page.on_view_pop = view_pop

    # # Start app at home
    # page.go("/")


ft.app(target=main)
