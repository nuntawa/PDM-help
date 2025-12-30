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

    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(margin=20, content=ft.Dropdown(
                label="ประเภทหน้าลูก",#สำหรับเมนูไม่ต้องมี  label ก็ได้
                options=[ 
                    ft.dropdown.Option(text="เลือกประเภทหน้าลูก", key="default",disabled=True),
                    ft.dropdown.Option(text="critiria", key="critiria"),
                    ft.dropdown.Option(text="ตาราง", key="critiria")
                ],
                # width=200
                expand=True,#เพื่อให้กว้าง  100%
            )),
            ft.ListTile(title=ft.Text("หน้าแม่"), on_click=lambda e:change_page("mother_page")),
            # ft.Divider(),
            ft.ListTile(title=ft.Text("Search Item"), on_click=lambda e:change_page("search_item_page")),
        ]
    )
    
    mother_page = mother_page_render(page)
    search_item_page = search_item_page_render(page)

    page_list={
        "mother_page":mother_page,
        "search_item_page":search_item_page
    }

    page.add(page_list["mother_page"])

ft.app(target=main)