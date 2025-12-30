import flet as ft


def main(page: ft.Page):
    page.title = "AppBar Example"
    page.scroll = "always"



    # def check_item_clicked(e):
    #     e.control.checked = not e.control.checked
    #     page.update()

    def change_page(page_name):
        page.controls.clear()
        page.add(page_list[page_name])
        page.close(drawer)
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("AppBar Example"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        leading=ft.IconButton(
                    icon=ft.Icons.MENU,
                    on_click=lambda e: page.open(drawer)
        )
    )
    drawer = ft.NavigationDrawer(
        # on_dismiss=handle_dismissal,
        # on_change=handle_change,
        controls=[
            ft.ListTile(title=ft.Text("Home"), on_click=lambda e:change_page("home")),
            ft.ListTile(title=ft.Text("Settings"), on_click=lambda e: change_page("settings")),
            ft.ListTile(title=ft.Text("About"), on_click=lambda e: change_page("about")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
            # ft.ListTile(title=ft.Text("About"), on_click=lambda e: print("click menu")),
        ],
    )
    
    home_row_input = ft.Row(
        controls=[
            ft.Text("Home Page", size=30),
        ]
    )
    settings_row_input = ft.Row(
        controls=[
            ft.Text("Settings Page", size=30),
        ]           
    )
    about_row_input = ft.Row(
        controls=[
            ft.Text("About Page", size=30),
        ]
    ) 

    page_list={
        "home":home_row_input,
        "settings":settings_row_input,
        "about":about_row_input
    }  

    page.add(ft.Text("Welcome"))
    # page.add(page_list["home"])
    # change_page("home")


ft.app(target=main)