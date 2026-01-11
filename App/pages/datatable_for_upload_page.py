import  flet as ft
def datatable_for_upload_page_render(page):

    row_1 = ft.Row(controls=[ft.Text("DatatableForUpload",size=15)])
    input_data = []

    def open_dlg(row_data):

        #header
        header_txt_field = ft.TextField(label="header *",expand=True,value="")

        #field
        field_txt_field = ft.TextField(label="field *",expand=True,value="")

        #width
        width_txt_field = ft.TextField(label="width",expand=True,value="10%")

        #sortable
        sortable_drop_down = ft.Dropdown(label="sortable *",options=[
            ft.dropdown.Option(text="true",key="true"),
            ft.dropdown.Option(text="false",key="false")
        ],value="false",expand=True)

        #align
        align_drop_down = ft.Dropdown(label="align *",options=[
            ft.dropdown.Option(text="left",key="left"),
            ft.dropdown.Option(text="center",key="center"),
            ft.dropdown.Option(text="right",key="right")
        ],value="left",expand=True)
        
        form = ft.Column(controls=[header_txt_field,field_txt_field,width_txt_field,sortable_drop_down,align_drop_down,error_display := ft.Text("",color="RED")])
    
        def save_form(e):
            if header_txt_field.value.strip() == "" or field_txt_field.value.strip() == "" or width_txt_field.value.strip() == "":
                error_display.value = "Please input all required element *"
                page.update()
                return
            else:
                error_display.value = ""
                page.update()


            if row_data is not None:
                #กรณีแก้ไข
                pass
            else:
                #กรณีเพิ่มใหม่
                input_data.append({
                    "header":header_txt_field.value,
                    "field":field_txt_field.value,
                    "width":width_txt_field.value,
                    "sortable":sortable_drop_down.value,
                    "align":align_drop_down.value
                })
            
            page.close(alert_dlg)
            render_row_page()
            

        alert_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Column"),
            content=ft.Container(
                width=600,
                height=300,
                content=form
            ),
            actions=[
                ft.TextButton("OK", on_click=save_form),
                ft.TextButton("Cancel", on_click=lambda e: page.close(alert_dlg))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(alert_dlg)
    
    add_input_btn = ft.FilledButton(text="Add Column",icon=ft.Icons.ADD_OUTLINED,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=200,on_click=lambda e: open_dlg(None))
    btn_row = ft.Row(controls=[add_input_btn])

    def render_row_page():
        row_control.controls.clear()
        row_control.controls.append(row_1)

        for idx, row_data in enumerate(input_data):
            row_control.controls.append(
                ft.Row(controls=[
                    ft.Text(f"{row_data['header']} | {row_data['field']} | {row_data['width']} | {row_data['sortable']} | {row_data['align']}",width=500),
                    ft.IconButton(icon=ft.Icons.EDIT,on_click=lambda e, rd=row_data: open_dlg(rd)),
                    ft.IconButton(icon=ft.Icons.DELETE_OUTLINE,on_click=lambda e, i=idx: (input_data.pop(i), render_row_page()))
                ])
            )

        row_control.controls.append(btn_row)
        page.update()

    row_control = ft.Column()
    render_row_page()

    return row_control