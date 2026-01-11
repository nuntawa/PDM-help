import flet as ft

def card_has_tab_render(page):

    row_1 = ft.Row(controls=[ft.Text("Card มี Tab",size=15)])

    text_field_arr = [
        ft.TextField(label="Tab name",width=800,value="`Accept Data (${acceptData?.totalRow?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')})`"),
        ft.TextField(label="Tab name",width=800,value="`Error Data (${errorData?.totalRow?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')})`")
    ]

    def gen_out_put(e):
        if len(text_field_arr) == 0:
            alert_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Can not generate code ! "),
                content=ft.Text("Please add at least one tab name."),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.open(alert_dlg)
            return
        
        #กรณีมี tab ที่ไม่ได้กรอกชื่อ
        for tf in text_field_arr:
            if tf.value.strip() == "":
                alert_dlg = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Can not generate code ! "),
                    content=ft.Text("Please input tab name."),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                page.open(alert_dlg)
                return
            
        import_str = """import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import Card from "primevue/card";"""
        import_field.value = import_str

        output_str = "<Card class=\"pdm-box\" >\n"
        output_str = output_str + " <template #content>\n       <div class=\"blue-tab-container\">\n            <TabView @tab-click=\"typeSwitch\" :v-model=\"activeIndex\">\n "

        for tf in text_field_arr:
            output_str = output_str + f"               <TabPanel :header=\"{tf.value}\">\n"
            output_str = output_str + "               </TabPanel>\n"


        output_str = output_str + "            </TabView>\n       </div>\n  </template>\n"
        output_str = output_str + "</Card>\n"

        output_str = output_str + "---------Script---------\n"
        output_str = output_str + "const activeIndex = ref(0);\n"

        output_str = output_str + """
const typeSwitch = (event) => {
  activeIndex.value = event.index;
};"""

        output_field.value = output_str
            
       

        page.update()
    
    ##end gen_out_put####

    # build rows dynamically from text_field_arr so indices remain correct after removals
    def remove_row(row_num):
        text_field_arr.pop(row_num)
        render_row_page()

    def add_input_row(_e):
        text_field_arr.append( ft.TextField(label="Tab name",value="",width=800) )
        render_row_page()
      
    ##end add_input_row ####

    def render_row_page():
        row_control.controls.clear()
        row_control.controls.append(row_1)
        for idx, tf in enumerate(text_field_arr):
            row_control.controls.append(
                ft.Row(controls=[tf,
                                 ft.FilledButton(
                                     text="Remove",
                                     icon=ft.Icons.DELETE_OUTLINE,
                                     style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
                                     width=100,
                                     on_click=lambda _e, row_num=idx: remove_row(row_num)
                                 )])
            )

        row_control.controls.append(row_btn)
        row_control.controls.append(row_import)
        row_control.controls.append(row_output)
        page.update()
    
    ##end render_row_page

    add_input_btn = ft.FilledButton(text="Add Tab",icon=ft.Icons.ADD_OUTLINED,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=add_input_row)


    #ปุ่ม generate code
    generate_code_btn = ft.FilledButton(text="Generate Code",icon=ft.Icons.CODE,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=150,on_click=gen_out_put)

    row_btn = ft.Row(controls=[add_input_btn, generate_code_btn])

    import_field = ft.TextField(label="Import",value=" ",min_lines=2,border_color="blue",multiline=True,
                                    expand=True,#ยาวเต็ม 100% 
    )
    row_import = ft.Row(controls=[import_field])

    output_field = ft.TextField(label="Code",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue")
    row_output = ft.Row(controls=[output_field])

    row_control = ft.Column()
    render_row_page()
    

    return row_control