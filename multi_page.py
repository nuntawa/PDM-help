import flet as ft

def main(page: ft.Page):
    page.title = "Multi-Page Desktop App"
    page.window_width = 500
    page.window_height = 400

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
                # ft.AppBar(title=ft.Text("🏠 Home Page"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.AppBar(title=ft.Text("🏠 Home Page") ),
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
                # ft.AppBar(title=ft.Text("⚙️ Settings"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.AppBar(title=ft.Text("⚙️ Settings")),
                ft.Text("This is the settings page.", size=18),
                ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
            ],
        )

    # ℹ️ About Page
    def view_about():
        return ft.View(
            "/about",
            [
                # ft.AppBar(title=ft.Text("ℹ️ About"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.AppBar(title=ft.Text("ℹ️ About")),
                ft.Text("Multi-page Flet desktop app example.", size=18),
                ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/")),
            ],
        )

    # Bind routing handlers
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Start app at home
    page.go("/")


ft.app(target=main)
