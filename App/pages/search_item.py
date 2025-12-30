import flet as ft

def search_item_page_render(page):

    def gen_out_put(e):
        if  label_field.value=="" or ref_field.value == "" or v_model_field.value == "" or company_id_field.value == "" :
            alert_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Can not generate code ! "),
                content=ft.Text("Please input all required element."),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.open(alert_dlg)
            return

        import_str = """import SearchItemPDM from "@/components/middle/SearchItem/search-itemPDM.vue";"""
        import_field.value = import_str

        output_str = f"<label>{{{{t("+label_field.value+f")}}}}</label>\n"
        output_str = output_str + f"<SearchItemPDM\n"
        output_str = output_str + f"    ref=\n"
        output_str = output_str + f"/>"
        output_field.value = output_str
        page.update()


    header_txt = ft.Text("Search Item", size=20)
    label_field = ft.TextField(label="Label *",value="ItemBasic.itemId")
    ref_field = ft.TextField(label="Ref *",value="SearchItemRef")
    v_model_field = ft.TextField(label="v-model *",value="itemObj")
    is_required_drop_down = ft.Dropdown(label="isRequired *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true")
    is_user_permission_drop_down = ft.Dropdown(label="isUserPermission *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true",width=130)
    company_id_field = ft.TextField(label="companyId *",value="route.params.companyId")


    gen_btn =  ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    import_field = ft.TextField(label="Import",value=" ",
                                    expand=True,#ยาวเต็ม 100%
                                    multiline=True,
                                    min_lines=3,
                                    # color="green" #สีตัวอักษร
                                    border_color="blue" #สีกรอบ 
                                )
    output_field = ft.TextField(label="Code",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue")

    row_1_header = ft.Row(controls=[header_txt])
    row_2_input = ft.Row(controls=[label_field,ref_field,v_model_field,is_required_drop_down])
    row_3_input =  ft.Row(controls=[is_user_permission_drop_down,company_id_field,gen_btn])
    row_4_output =  ft.Row(controls=[import_field])
    row_5_output =  ft.Row(controls=[output_field])


    row_control = ft.Column(
        controls=[
            row_1_header,
            row_2_input,
            ft.Container(margin=ft.margin.only(top=12),content=row_3_input),#ให้ห่างจากด้านบน 10
            row_4_output,
            row_5_output
        ]
    )





    return row_control