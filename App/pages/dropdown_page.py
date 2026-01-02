import flet as ft 

def dropdown_page_render(page):

    row_1 = ft.Row(controls=[
        ft.Text("Dropdown",size=15)
    ])

    row_control = ft.Column(
        controls=[
            row_1
        ]
    )

    return row_control