import flet as ft 

def dropdown_page_render(page):

    def gen_out_put(e):
        if label_text_field.value == "" or options_text_field.value == "" or option_label_field.value == "" or option_value_field.value == "" or v_model_txt_field.value == "" or ref_txt_field.value == ""  or empty_message_txt_field.value == "" :
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

        import_str = """import Dropdown from "primevue/dropdown";"""
        import_field.value = import_str

        #เพิ่ม  tag required ( ดอกจันทร์แดง )
        required_tag = ""
        if is_required_drop_down.value == "true":
            required_tag = "<small class=\"font-red\"> * </small>"


        #สรา้ง Element
        output_str = f"<label>{{{{ t("+label_text_field.value+f") }}}} {required_tag} </label>\n" #ต้องใช้ {{{{  4 ตัว สำหรับ {{ ใน vue 
        output_str = output_str + f"<Dropdown\n"
        output_str = output_str + f"    :options=\"{options_text_field.value}\"\n"
        output_str = output_str + f"    optionLabel=\"{option_label_field.value}\"\n"
        output_str = output_str + f"    optionValue=\"{option_value_field.value}\"\n"
        output_str = output_str + f"    placeholder=\"t('"+ placeholder_text_field.value +"')\"\n"
        output_str = output_str + f"    :filter=\"{filter_drop_down.value}\"\n"
        output_str = output_str + f"    :showClear=\"{show_clear_drop_down.value}\"\n"
        output_str = output_str + f"    v-model=\"{v_model_txt_field.value}\"\n"
        output_str = output_str + f"    ref=\"{ref_txt_field.value}\"\n"
        output_str = output_str + f"    :emptyMessage=\"t('"+ empty_message_txt_field.value +"')\"\n"
        output_str = output_str + f""
        output_str = output_str + f"    @hide=\"()=>checkDropDownHide({ref_txt_field.value})\" \n"
        output_str = output_str + f"    @change=\"()=>{v_model_txt_field.value}Change()\" \n"
        output_str = output_str + f"/>\n"

        output_str = output_str + """
                        <template #option="slotProps">
                          <a
                            v-tooltip.top="slotProps.option."""+option_label_field.value+""""
                            class="text-ellipsis w-full"
                          >
                            {{ slotProps.option."""+option_label_field.value+""" }}&nbsp;
                          </a>
                        </template>
        """

        output_str = output_str + "</Dropdown>\n"
        output_str = output_str + """
                <div class="display-error-row">
                    <small class="input-error text-ellipsis">
                        <!-- Error Message -->
                    </small>
                </div>
        """

        output_str = output_str + f"<!--------------<script setup>-------------->\n"
        output_str = output_str + f"const {ref_txt_field.value} = ref();\n"
        output_str = output_str + f"const {v_model_txt_field.value} = ref();\n"

        output_str = output_str + """
        const checkDropDownHide = (objRef)=>{
            objRef.filterValue = "";
        }\n"""


        output_str = output_str + f"const {v_model_txt_field.value}Change = ()=>{{\n"

        if is_required_drop_down.value == "true":
            output_str = output_str + f"""    if(!{v_model_txt_field.value}.value){{\n"""
            output_str = output_str + f"""     // Show error message \n"""
            output_str = output_str + f"""    }}\n"""
       
        output_str = output_str + f"}};\n"




        output_field.value = output_str

        page.update()

    row_1 = ft.Row(controls=[
        ft.Text("Dropdown",size=15)
    ])

    label_text_field = ft.TextField(label="label",value="ItemBasic.deliveryType")
    is_required_drop_down = ft.Dropdown(label="isRequired *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true")
    options_text_field = ft.TextField(label="options * ",value="props.dataFromAPI....")
    option_label_field = ft.TextField(label="optionLabel * ",value="name",width=150)
    option_value_field = ft.TextField(label="optionValue * ",value="value",width=150)

    placeholder_text_field = ft.TextField(label="placeholder",value="**ถ้า  required** pleaseSelect")
    filter_drop_down = ft.Dropdown(label="filter *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true")
    show_clear_drop_down = ft.Dropdown(label="showClear *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true")
    v_model_txt_field = ft.TextField(label="v-model * ",value="deliveryTypeSelect")
    ref_txt_field = ft.TextField(label="ref * ",value="deliveryTypeSelectRef")

    empty_message_txt_field = ft.TextField(label="emptyMessage *",value="No ...")

    gen_btn =  ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    
    import_field = ft.TextField(label="Import",value=" ",min_lines=2,border_color="blue",multiline=True,
                                    expand=True,#ยาวเต็ม 100%
    )
    output_field = ft.TextField(label="Code",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue") 

    row_2 = ft.Row(controls=[label_text_field,is_required_drop_down,options_text_field,option_label_field,option_value_field])
    row_3 = ft.Row(controls=[placeholder_text_field,filter_drop_down,show_clear_drop_down,v_model_txt_field,ref_txt_field])
    row_4 = ft.Row(controls=[empty_message_txt_field,gen_btn])
    row_5 = ft.Row(controls=[import_field])
    row_6 = ft.Row(controls=[output_field])

    row_control = ft.Column(
        controls=[
            row_1,row_2,row_3,row_4,row_5,row_6
        ]
    )

    return row_control