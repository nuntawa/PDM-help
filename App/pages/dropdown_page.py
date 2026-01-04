import flet as ft 

def dropdown_page_render(page):

    row_1 = ft.Row(controls=[
        ft.Text("Dropdown",size=15)
    ])

    label_text_field = ft.TextField(label="label",value="ItemBasic.deliveryType")
    is_required_drop_down = ft.Dropdown(label="isRequired *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true")

    row_2 = ft.Row(controls=[label_text_field,is_required_drop_down])

    row_control = ft.Column(
        controls=[
            row_1,row_2
        ]
    )

    return row_control