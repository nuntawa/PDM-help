import flet as ft

def button_page_render(page):

    def gen_out_put(e):

        import_field.value = "import ButtonPDM from \"@/components/middle/Button/buttonPDM.vue\";"

        selected_type = []
        for cb in checkboxes:
            if cb.value:
                selected_type.append(cb.key)

        if len(selected_type) == 0: #กรณีไม่เลือกประเภทปุ่มเลย
            alert_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Can not generate code ! "),
            content=ft.Text("กรุณาเลือกประเภทปุ่มอย่างน้อย 1 ประเภท"),
            actions=[
                ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            )
            page.open(alert_dlg)
            return
        
        output_str = ""
        content_end = False
        for btn_type in selected_type:
            if btn_type == "content-end":
                output_str = output_str + f"<div class=\"flex justify-content-end\">\n"
                content_end = True
            else:
                output_str = output_str + f"    <ButtonPDM\n"


                output_str = output_str + f"         :onClick=\"()=>{{ ... }}\"\n"
                output_str = output_str + f"    />\n\n"
        #end for

        if content_end:
            output_str = output_str + f"</div>"

        # output_str = f"<ButtonPDM\n"
        # output_str = output_str + f"    type=\"{button_type_dropdown.value}\"\n"
        # output_str = output_str + f"/>\n"

        # # output_field.value = output_str

        #<div class="flex justify-content-end"></div>
        output_field.value = output_str
        page.update()

    row_1 = ft.Row(controls=[
        ft.Text("Button",size=15)
    ])

    #ตัวเลือกประเภทปุ่ม
    options = [
        ("ปุ่มด้านล่าง", "content-end"),
        ("Search", "search"),
        ("Save", "save"),
        ("Delete", "delete"),
        ("Clear", "clear"),
        ("Report", "report"),
        ("Generate", "generate"),
    ]

    checkboxes = []

    for text, key in options:
        cb = ft.Checkbox(label=text, value=False, key=key)#, on_change=_on_checkbox_changed)
        checkboxes.append(cb)

     
    button_type_check_box = ft.Container(content=ft.Row(controls=checkboxes))

    gen_btn = ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    row_2 = ft.Row(controls=[button_type_check_box,gen_btn])

    import_field = ft.TextField(label="Import",value=" ",min_lines=2,border_color="blue",multiline=True,
                                    expand=True,#ยาวเต็ม 100%
    )
    row_3 = ft.Row(controls=[import_field])
    output_field = ft.TextField(label="Code",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue") 
    row_4 = ft.Row(controls=[output_field])

    row_control = ft.Column(
        controls=[
            row_1,
            row_2,
            row_3,
            row_4
        ],
    )

    return row_control