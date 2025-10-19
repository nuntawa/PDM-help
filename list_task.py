import flet as ft

def main(page):
    
    page.title = "List Task  งาน"
    #หัว radio  group
    # text_radio_group_header = ft.Text("ประเภทหน้า")

    # page_type_radio_group = ft.RadioGroup(
    #     content=ft.Row(
    #         [
    #             ft.Radio(value="หน้าแม่", label="หน้าแม่"),
    #             ft.Radio(value="หน้าลูก", label="หน้าลูก"),
    #         ]
    #     )
    # )


    # page.add(text_radio_group_header,page_type_radio_group)

    
    # def create_tab_drop_down():
        
        
    tab_drop_down = ft.Dropdown(
            label="ประเภท Tab ",
            options=[ 
                ft.dropdown.Option(text="เลือกประเภท Tab", key="default"),
                ft.dropdown.Option(text="Maintenance", key="Maintenance"),
                ft.dropdown.Option(text="Upload", key="Upload")
            ],
            width=180
        )
    tab_drop_down.value ="default"

    page_type_drop_down = ft.Dropdown(
        label="ประเภทหน้า",
         options=[ 
            ft.dropdown.Option(text="หน้าแม่", key="หน้าแม่"),
            ft.dropdown.Option(text="หน้าลูก", key="หน้าลูก")
        ],
        width=180
    )

    child_type_drop_down = ft.Dropdown(
        label="ประเภทหน้าลูก",
         options=[ 
            ft.dropdown.Option(text="critiria", key="critiria"),
            ft.dropdown.Option(text="ตาราง", key="critiria")
        ],
        width=180
    )

    function_drop_down = ft.Dropdown(
        label="Function",
         options=[ 
            ft.dropdown.Option(text="สร้าง Control", key="สร้าง Control"),
            ft.dropdown.Option(text="สร้าง", key="สร้าง"),
            ft.dropdown.Option(text="Function Validate", key="Function Validate"),
            ft.dropdown.Option(text="Function", key="Function"),
            ft.dropdown.Option(text="เรียก  API", key="เรียก  API")
        ],
        width=180
    )

    description_field = ft.TextField(width=270)
    
    def gen_out_put(e):#function  สร้าง output
        out_put_field.value = tab_drop_down.value
        page.update()#ต้องมี  Update  ด้วย

    gen_btn =  ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    def clear_input(e):
        description_field.value ="default"
        tab_drop_down.value = ""
        # tab_drop_down.value = ""
        # page_type_drop_down.value = ""
        # child_type_drop_down.value = ""
        # function_drop_down.value = ""

        
        #Update all components
        tab_drop_down.update()
        page.update()#ต้องมี  Update  ด้วย
        

    clear_btn =  ft.FilledButton(text="Clear",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
     ),width=100,on_click=clear_input)

    row_input_control = ft.Row(controls=[tab_drop_down,
                                        page_type_drop_down,
                                        child_type_drop_down,
                                        function_drop_down,
                                        description_field,
                                        gen_btn,
                                        clear_btn
                                        ])
    out_put_field = ft.TextField(
        expand=True,  # This makes the TextField expand to fill available width
        multiline=True,
        min_lines=5)
    
    row_out_put_control = ft.Row(controls=[out_put_field])

    

    page.add(row_input_control)
    page.add(row_out_put_control)

ft.app(target=main)