import flet as ft
from pages.mother_page import mother_page_render
from pages.search_item import search_item_page_render
from pages.dropdown_page import dropdown_page_render
from pages.button_page import button_page_render    

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
            menu_column.controls.append(
                ft.ListTile(title=ft.Text("Dropdown"), on_click=lambda e:change_page("dropdown_page")),
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
    #array ที่เป็น dictionary เก็บเมนูทั้งหมด
    menu_list = [
        {"group":"layout","name":"หน้าแม่","page":"mother_page"},
        {"group":"component","name":"Search Item","page":"search_item_page"},
        {"group":"component","name":"Dropdown","page":"dropdown_page"},
        {"group":"component","name":"Button","page":"button_page"}
    ]

    for menu_item in menu_list:
        menu_column.controls.append(
            ft.ListTile(title=ft.Text(menu_item["name"]), on_click=lambda _e, page=menu_item["page"]: change_page(page)),
        )

    # menu_column.controls.append(
    #     ft.ListTile(title=ft.Text("หน้าแม่"), on_click=lambda e:change_page("mother_page")),
    # )
    # menu_column.controls.append(
    #     ft.ListTile(title=ft.Text("Search Item"), on_click=lambda e:change_page("search_item_page")),
    # )
    # menu_column.controls.append(
    #     ft.ListTile(title=ft.Text("Dropdown"), on_click=lambda e:change_page("dropdown_page")),
    # )
    # menu_column.controls.append(
    #     ft.ListTile(title=ft.Text("Button"),on_click=lambda e:change_page("button_page")),
    # )
    
    drawer = ft.NavigationDrawer(
        controls=[
            menu_group_dropdown,
            menu_column
        ]
    )
    
    mother_page = mother_page_render(page)
    button_page = button_page_render(page)
    search_item_page = search_item_page_render(page)
    dropdown_page = dropdown_page_render(page)

    #เก็บหน้าต่างๆ
    page_list={
        "mother_page":mother_page,
        "search_item_page":search_item_page,
        "dropdown_page":dropdown_page,
        "button_page":button_page,
    }

    page.add(page_list["mother_page"])

ft.app(target=main)