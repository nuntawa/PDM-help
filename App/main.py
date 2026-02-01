import flet as ft
from pages.mother_page import mother_page_render
from pages.search_item import search_item_page_render
from pages.dropdown_page import dropdown_page_render
from pages.button_page import button_page_render
from pages.file_upload_page import file_upload_page_render
from pages.card_has_tap import card_has_tab_render
from pages.datatable_for_upload_page import datatable_for_upload_page_render
from pages.grid_page import grid_page_render
from pages.calendar_page import calendar_page_render

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

        for menu_item in menu_list:
            if menu_item["group"] == menu_group_select_dropdown.value:
                menu_column.controls.append(
                    ft.ListTile(title=ft.Text(menu_item["name"]), on_click=lambda _e, page=menu_item["page"]: change_page(page)),#ใส่ page=menu_item["page"]  เพื่อแก้ปัญหา lambda ดึงค่าผิด
                )
        page.update()     
    ### end def ####################################################################    

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
        {"group":"layout","name":"Card มี  Tab (เช่น  Upload)","page":"card_has_tab_page"},
        {"group":"component","name":"Search Item","page":"search_item_page"},
        {"group":"component","name":"Dropdown","page":"dropdown_page"},
        {"group":"component","name":"Button","page":"button_page"},
        {"group":"component","name":"File Upload","page":"file_upload_page"},
        {"group":"component","name":"DatatableForUpload","page":"datatable_for_upload_page"},
        {"group":"layout","name":"Grid","page":"grid_page"},
        {"group":"component","name":"Calendar","page":"calendar_page"},
    ]

    for menu_item in menu_list:
        if menu_item["group"] == "layout":#แสดงเมนูแรกเป็นกลุ่ม layout
            menu_column.controls.append(
                ft.ListTile(title=ft.Text(menu_item["name"]), on_click=lambda _e, page=menu_item["page"]: change_page(page)),
            )

    
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
    file_upload_page = file_upload_page_render(page)
    card_has_tab_page = card_has_tab_render(page)
    datatable_for_upload_page = datatable_for_upload_page_render(page)
    grid_page = grid_page_render(page)
    calendar_page = calendar_page_render(page)

    #เก็บหน้าต่างๆ
    page_list={
        "mother_page":mother_page,
        "search_item_page":search_item_page,
        "dropdown_page":dropdown_page,
        "button_page":button_page,
        "file_upload_page":file_upload_page,
        "card_has_tab_page":card_has_tab_page,
        "datatable_for_upload_page":datatable_for_upload_page,
        "grid_page":grid_page,
        "calendar_page":calendar_page,
    }

    def show_error(title,text):
        alert_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text(title),
                content=ft.Text(text),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(alert_dlg)

    page.show_error = show_error
    page.add(page_list["mother_page"])

ft.app(target=main)