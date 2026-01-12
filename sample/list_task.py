import flet as ft

def main(page):
    
    page.title = "List Task  งาน"
    page.scroll = "always"
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
                ft.dropdown.Option(text="เลือกประเภท Tab", key="default",disabled=True),
                ft.dropdown.Option(text="Maintenance", key="Maintenance"),
                ft.dropdown.Option(text="Upload", key="Upload"),
                ft.dropdown.Option(text="Add Item", key="Add Item")
            ],
            width=180
        )

    page_type_drop_down = ft.Dropdown(
        label="ประเภทหน้า",
         options=[ 
            ft.dropdown.Option(text="ประเภทหน้า", key="default",disabled=True),
            ft.dropdown.Option(text="หน้าแม่", key="หน้าแม่"),
            ft.dropdown.Option(text="หน้าลูก", key="หน้าลูก")
        ],
        width=180
    )

    child_type_drop_down = ft.Dropdown(
        label="ประเภทหน้าลูก",
         options=[ 
            ft.dropdown.Option(text="เลือกประเภทหน้าลูก", key="default",disabled=True),
            ft.dropdown.Option(text="critiria", key="critiria"),
            ft.dropdown.Option(text="ตาราง", key="critiria")
        ],
        width=200
    )

    function_drop_down = ft.Dropdown(
        label="Function",
         options=[ 
            ft.dropdown.Option(text="เลือก Function", key="default",disabled=True),
            ft.dropdown.Option(text="สร้าง Control", key="สร้าง Control"),
            ft.dropdown.Option(text="Control", key="Control"),
            ft.dropdown.Option(text="สร้าง", key="สร้าง"),
            ft.dropdown.Option(text="สร้าง Function", key="สร้าง Function"),
            ft.dropdown.Option(text="Function Validate", key="Function Validate"),
            ft.dropdown.Option(text="Function", key="Function"),
            ft.dropdown.Option(text="เรียก  API", key="เรียก  API")
        ],
        width=180
    )

    description_field = ft.TextField(width=340)
    
    def gen_out_put(e):#function  สร้าง output

        out_put = out_put_field.value
        flag = 0

        if tab_drop_down.value != "default" :
            out_put = out_put +"Tab "+tab_drop_down.value+" "
            flag = 1

        if page_type_drop_down.value != "default" :
            out_put = out_put + page_type_drop_down.value+" "
            flag = 1
        
        if child_type_drop_down.value != "default" :
            out_put = out_put + child_type_drop_down.value+" "
            flag = 1

        if function_drop_down.value != "default" :
            out_put = out_put + function_drop_down.value+" "
            flag = 1

        if description_field.value != "" :
            out_put = out_put + description_field.value+" "
            flag = 1

        if flag != 0 :
            out_put = out_put + "\n"

        out_put_field.value = out_put

        page.update()#ต้องมี  Update  ด้วย
        clear_input(None)

    gen_btn =  ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    def clear_input(e):
        description_field.value =""
        tab_drop_down.value = "default"
        page_type_drop_down.value = "default"
        child_type_drop_down.value = "default"
        function_drop_down.value = "default"
        page.update()#ต้องมี  Update  ด้วย
        

    clear_btn =  ft.FilledButton(text="Clear",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
     ),width=100,on_click=clear_input)

    row_input_control = ft.Row(controls=[tab_drop_down,
                                        page_type_drop_down,
                                        child_type_drop_down,
                                        function_drop_down,
                                        description_field,
                                        
                                        ])
    row_button_control = ft.Row(controls=[gen_btn,clear_btn])
    out_put_field = ft.TextField(
        expand=True,  # This makes the TextField expand to fill available width
        multiline=True,
        min_lines=5)
    
    # row_out_put_control = ft.Row(controls=[
    #         ft.Container(
    #             content=out_put_field,
    #             scroll="always", # Enables scrolling for this column
    #             expand=True,     # Makes it take up available space
    #         ),
    # ])

    row_out_put_control = ft.Row(controls=[out_put_field])
    

    clear_input(None)#กำหนดค่า  Default

    page.add(row_input_control)
    page.add(row_button_control)
    page.add(row_out_put_control)

ft.app(target=main)