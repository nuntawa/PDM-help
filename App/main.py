import flet as ft
from pages.mother_page import mother_page_render
from pages.search_item import search_item_page_render

def main(page: ft.Page):
    page.title = "PDM"
    page.scroll = "always"
    
    def change_page(page_name):
        page.controls.clear()
        page.add(page_list[page_name])
        page.close(drawer)
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("PDM"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        leading=ft.IconButton(
                    icon=ft.Icons.MENU,
                    on_click=lambda e: page.open(drawer)
        )
    )
    
    #ซ่อน แสดงกลุ่ม เมนู
    def show_hide_menu(e):
        # print("show hide menu")
        menu_column.controls.clear()
        if menu_group_select_dropdown.value == "layout":
            menu_column.controls.append(
                ft.ListTile(title=ft.Text("หน้าแม่"), on_click=lambda e:change_page("mother_page")),
            )
        elif menu_group_select_dropdown.value == "component":
            menu_column.controls.append(
                ft.ListTile(title=ft.Text("Search Item"), on_click=lambda e:change_page("search_item_page")),
            )

        page.update()     
    #######################################################################    

    menu_group_select_dropdown = ft.Dropdown(
                label="ประเภทเมนู",#สำหรับเมนูไม่ต้องมี  label ก็ได้
                options=[ 
                    ft.dropdown.Option(text="เลือกประเภทเมนู", key="default",disabled=True),
                    ft.dropdown.Option(text="Layout", key="layout"),
                    ft.dropdown.Option(text="Component", key="component")
                ],
                # width=200
                expand=True,#เพื่อให้กว้าง  100%
                on_change=show_hide_menu
    )
    menu_group_dropdown =ft.Container(margin=20, content=menu_group_select_dropdown)
    

    menu_column = ft.Column(
                expand=True,
                controls=[]
    )
    menu_column.controls.append(
        ft.ListTile(title=ft.Text("หน้าแม่"), on_click=lambda e:change_page("mother_page")),
    )
    menu_column.controls.append(
        ft.ListTile(title=ft.Text("Search Item"), on_click=lambda e:change_page("search_item_page")),
    )
    
    drawer = ft.NavigationDrawer(
        controls=[
            menu_group_dropdown,
            menu_column
        ]
    )
    
    mother_page = mother_page_render(page)
    search_item_page = search_item_page_render(page)

    #เก็บหน้าต่างๆ
    page_list={
        "mother_page":mother_page,
        "search_item_page":search_item_page
    }

    page.add(page_list["mother_page"])

ft.app(target=main)