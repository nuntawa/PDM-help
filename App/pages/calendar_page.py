import flet as ft
def calendar_page_render(page: ft.Page):

    def gen_out_put(e):
        if v_model_field.value == "" or label_field.value == "" or min_date_field.value == "" or max_date_field.value == "":
            alert_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Can not generate code ! "),
                content=ft.Text("Please input all required elements."),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.close(alert_dlg)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.open(alert_dlg)
            return
        
        import_str = """import Calendar from "@/components/middle/CustomCalendar/CustomCalendarV2";
import { useDateFormat } from "@vueuse/core";"""

        required_tag = ""
        if  is_required_drop_down.value=="true":
            required_tag = "<small class=\"font-red\"> * </small>"

         #กำหนดชื่อ  function ตรวจสอบวันที่
        f_name = v_model_field.value[0].upper() + v_model_field.value[1:]

        #สร้าง Element
        output_str = f"""
        <label>{{{{ t('{label_field.value}') }}}} { required_tag }</label>\n
        <div>
            <Calendar
                style="width: 100%; height: 32px"
                class="general-input"
                dateFormat="dd/mm/yy"
                v-model="{v_model_field.value}"
                :showIcon="true"
                :maxDate="{max_date_field.value}"
                :minDate="{min_date_field.value}"
                :placeholder="t('ItemBasic.dateFormat')"
                @input="() => {{check{f_name}()}}"
                @blur="()=>{{check{f_name}()}}"
                @focus="()=>{{check{f_name}()}}"
                @keydown="()=>{{check{f_name}()}}"
            />
        </div>
        <div class="display-error-row">
                 <small class="input-error" v-if="error.{v_model_field.value}" >
                    <!-- แสดงข้อความ error --/>
                 </small>
        </div>
        """

       
        
        #สร้างตัวแปร และ function
        output_str = output_str + f"<!--------------<script setup>-------------->\n"
        output_str = output_str + f"const {v_model_field.value} = ref();\n"
        output_str = output_str + f"const {min_date_field.value} = ref();\n"
        output_str = output_str + f"const {max_date_field.value} = ref();\n"
        output_str = output_str + f"const check{f_name} () =>{{\n"
        output_str = output_str + """
            // end date  อยู่ก่อน  start  date
    if(  [start_date_obj].value && [end_date_obj].value )
    {
        //start มากกว่า end
        if( parseInt(useDateFormat([start_date_obj].value,'YYYYMMDD').value) > parseInt(useDateFormat([end_date_obj].value,'YYYYMMDD').value) )
        {
           
            //แสดง  error
            return;
        }
        else
        {
            // clear error
        }
    }
        """
        output_str = output_str + f"}}\n"

        output_field.value = output_str
        import_field.value = import_str

        page.update()
    ########## end gen output ##########

    gen_btn = ft.FilledButton(text="Generate",icon=ft.Icons.CODE,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),width=150
                                ,on_click=lambda e: gen_out_put(e))
    
    is_required_drop_down = ft.Dropdown(label="isRequired *",options=[
        ft.dropdown.Option(text="true",key="true"),
        ft.dropdown.Option(text="false",key="false")
    ],value="true")

    label_field = ft.TextField(label="label *",value="effectiveStartDate")
    v_model_field = ft.TextField(label="v-model *",value="effectiveStartDate")
    min_date_field = ft.TextField(label="minDate *",value="minDate",width=150)
    max_date_field = ft.TextField(label="maxDate *",value="maxDate",width=150)

    row_input = ft.Row(controls=[label_field,v_model_field,is_required_drop_down,min_date_field,max_date_field])
    import_field = ft.TextField(label="Import",value=" ",multiline=True,expand=True,min_lines=2,border_color="blue")
    output_field = ft.TextField(label="Code",value=" ",multiline=True,expand=True,min_lines=10,border_color="blue")
        

    row_controls = ft.Column(controls=[
        ft.Text("Calendar",size=15),
        row_input,
        gen_btn,
        import_field,
        output_field
    ])

    return row_controls