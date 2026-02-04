import flet as ft
def grid_page_render(page):

    input_data = []

    def gen_out_put():
        if len(input_data) == 0:
            page.show_error("Error","Can not generate code ! Please add at least one column.")
            return
        
        no_padding_grid_bottom = ""
        no_padding_grid_top = ""
        for cb in checkbox_class:
            if cb.key == "no-padding-grid-bottom" and cb.value:
                no_padding_grid_bottom = " no-padding-grid-bottom"
            if cb.key == "no-padding-grid-top" and cb.value:
                no_padding_grid_top = " no-padding-grid-top"

        output_str = f"<div class=\"grid\">\n"

        for row in input_data:
            flex_class = ""
            if row['flex_class']:
                flex_class = " flex align-items-center"
            output_str = output_str + f"    <div class=\"col-{row['column_n']} {no_padding_grid_bottom} {no_padding_grid_top} {flex_class}\">\n"
            output_str = output_str + f"      { '<!--  สำหรับปุ่ม  search-->' if flex_class != '' else '' }   \n"
            output_str = output_str + "    </div>\n"
        
        output_str = output_str + "</div>\n"
        output_field.value = output_str
        page.update()

    ##---end gen_out_put---

    def open_dlg(row_data):

        #ฟอร์มกรอกข้อมูล

        flex_check_box = ft.Checkbox(label="flex align-items-center ( กรณี column  สุดท้ายเป็นปุ่ม )", value=False,key="flex align-items-center")
        column_n_dropdown = ft.Dropdown(label="Column N *",options=[
            ft.dropdown.Option(text="1",key="1"),
            ft.dropdown.Option(text="2",key="2"),
            ft.dropdown.Option(text="3",key="3"),
            ft.dropdown.Option(text="4",key="4"),
            ft.dropdown.Option(text="5",key="5"),
            ft.dropdown.Option(text="6",key="6"),
            ft.dropdown.Option(text="7",key="7"),
            ft.dropdown.Option(text="8",key="8"),
            ft.dropdown.Option(text="9",key="9"),
            ft.dropdown.Option(text="10",key="10"),
            ft.dropdown.Option(text="11",key="11"),
            ft.dropdown.Option(text="12",key="12"),
        ],value="3",expand=True)
        form_column = ft.Column(controls=[column_n_dropdown,flex_check_box])

        # กรณีแก้ไข ให้ set ค่าเดิม
        if row_data is not None:
            flex_check_box.value = row_data['flex_class']
            column_n_dropdown.value = row_data['column_n']
        
        
        def save_form(e):
            if row_data is None:
                #กรณีเพิ่มใหม่
                input_data.append({
                    "flex_class": flex_check_box.value,
                    "column_n": column_n_dropdown.value
                })
            else:
                #กรณีแก้ไข
                row_data['flex_class'] = flex_check_box.value
                row_data['column_n'] = column_n_dropdown.value

            page.close(alert_dlg)
            render_row_control()
            

        alert_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Column"),
            content=ft.Container(
                width=350,
                height=180,
                content=form_column
            ),
            actions=[
                ft.TextButton("OK", on_click=save_form),
                ft.TextButton("Cancel", on_click=lambda e: page.close(alert_dlg) ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(alert_dlg)

    def render_row_control():
        row_control.controls.clear()
        row_control.controls.append(ft.Text("Grid", size=15))
        checkbox_class_container = ft.Container(content=ft.Row(controls=checkbox_class))
        
        if len(input_data) >0:

            #สรา้ง Header
            row_control.controls.append(
                ft.Container(content=
                    ft.Row(controls=[
                        ft.Container(content=ft.Text("flex align-items-center",weight="bold",color="BLUE"),width=180),
                        ft.Container(content=ft.Text("Column N",weight="bold",color="BLUE"),width=180),
                        ft.Container(content=ft.Text("Action",weight="bold",color="BLUE"),width=200),
                    ],height=25)
            ))
            row_control.controls.append(ft.Divider())

            for idx,row in enumerate(input_data):
                row_control.controls.append(ft.Container(
                    content=ft.Row(controls=[
                        ft.Container(content=ft.Text(str(row['flex_class'])),width=180),
                        ft.Container(content=ft.Text(str(row['column_n'])),width=180),
                        ft.Container(content=ft.Row(controls=[
                            ft.FilledButton(text="Edit",icon=ft.Icons.EDIT_OUTLINED,width=100,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                            on_click=lambda e, row=row: open_dlg(row) ),
                            ft.FilledButton(text="Delete",icon=ft.Icons.DELETE_OUTLINE,width=100,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                            on_click=lambda e,
                                            idx=idx: (input_data.pop(idx),render_row_control()) ),
                        ]),width=200),
                    ],height=25)
                ))
                row_control.controls.append(ft.Divider())


        row_control.controls.append(checkbox_class_container)
        row_control.controls.append(btn_row)

        if( len(input_data) != 0 ): #มีข้อมูลแล้วสร้าง output 
            row_control.controls.append(output_field)
            
        page.update()
    #-----end render_row_control-------

    checkbox_class = [
        ft.Checkbox(label="no-padding-grid-bottom", value=False,key="no-padding-grid-bottom"),
        ft.Checkbox(label="no-padding-grid-top ( แถวแรกไม่ต้องมี )", value=False,key="no-padding-grid-top")
    ]



    #ปุ่มเพิ่มแถว
    add_input_btn = ft.FilledButton(text="Add Column",icon=ft.Icons.ADD_OUTLINED,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=200,on_click=lambda e: open_dlg(None))
    #ปุ่ม  gen output
    gen_btn = ft.FilledButton(text="Generate",icon=ft.Icons.CODE,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=200,on_click=lambda e: gen_out_put())

    btn_row = ft.Row(controls=[add_input_btn,gen_btn])

    output_field = ft.TextField(label="Output",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue")


    row_control = ft.Column()
    render_row_control()
    return row_control