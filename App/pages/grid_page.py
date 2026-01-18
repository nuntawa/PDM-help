import flet as ft
def grid_page_render(page):

    input_data = []
    def open_dlg(row_data):
        alert_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Column"),
            content=ft.Container(
                width=600,
                height=300,
                content=ft.Text("Form Column")
            ),
            actions=[
                ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
                ft.TextButton("Cancel", on_click=lambda e: page.close(alert_dlg))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(alert_dlg)

    def render_row_control():
        row_control.controls.clear()
        row_control.controls.append(ft.Text("Grid", size=15))

        row_control.controls.append(add_input_btn)
        page.update()

    #ปุ่มเพิ่มแถว
    add_input_btn = ft.FilledButton(text="Add Column",icon=ft.Icons.ADD_OUTLINED,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=200,on_click=lambda e: open_dlg(None))

    row_control = ft.Column()
    render_row_control()
    return row_control