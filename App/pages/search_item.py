import flet as ft

def search_item_page_render(page):

    def gen_out_put():
        pass

    header_txt = ft.Text("Search Item", size=20)
    ref_field = ft.TextField(label="Ref",value="SearchItemRef")
    v_model_field = ft.TextField(label="v-model",value="itemObj")
    is_required_drop_down = ft.Dropdown(label="isRequired",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true",enable_filter=True)
    is_user_permission_drop_down = ft.Dropdown(label="isUserPermission",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true",enable_filter=True)
    company_id_field = ft.TextField(label="companyId",value="route.params.companyId")


    gen_btn =  ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)


    row_1_header = ft.Row(controls=[header_txt])
    row_2_input = ft.Row(controls=[ref_field,v_model_field,is_required_drop_down,is_user_permission_drop_down,company_id_field])
    row_3_button = ft.Row(controls=[gen_btn])


    row_control = ft.Column(
        controls=[
            row_1_header,
            row_2_input,
            row_3_button
        ]
    )





    return row_control