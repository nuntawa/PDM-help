import flet as ft
def calendar_page_render(page: ft.Page):

    gen_btn = ft.FilledButton(text="Generate",icon=ft.Icons.CODE,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),width=150
                                ,on_click=lambda e: None)

    row_controls = ft.Column(controls=[
        ft.Text("Calendar",size=15),

        gen_btn
    ])

    return row_controls