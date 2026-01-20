import  flet as ft
def datatable_for_upload_page_render(page):

    row_1 = ft.Row(controls=[ft.Text("DatatableForUpload",size=15)])
    input_data = []

    def gen_out_put(e):
        if(len(input_data) == 0):
            page.show_error("Error","No column defined.")
            return
        
        import_str = "import DatatableForUpload from \"@/components/middle/DataTableForUpload/datatable-for-uploadV2.vue\";"
        import_field.value = import_str
        
        output_str = """<DatatableForUpload
    ref="AcceptTableRef"
    :hideFilterText="false /* ซ่อนค้นหาตาม  text box หรือไม่ */
    :tableStructure="[\n"""

        for idx,col in enumerate(input_data):
            output_str = output_str + "         {\n"
            output_str = output_str + f"             header: '{col['header']}', /* ชื่อหัวตาราง */\n"
            output_str = output_str + f"             field: '{col['field']}', /* ชื่อฟิลด์ข้อมูล */\n"
            output_str = output_str + f"             width: '{col['width']}', /* ความกว้าง เช่น  '10%' , '100px' */\n"
            output_str = output_str + f"             sortable: {col['sortable']}, /* สามารถเรียงลำดับได้หรือไม่  true/false */\n"
            output_str = output_str + f"             align: '{col['align']}' /* การจัดตำแหน่ง  left/center/right */\n"
            output_str = output_str + "         }"

            if idx != len(input_data)-1:
                output_str = output_str + ",\n"#ใส่ comma ถ้าไม่ใช่ตัวสุดท้าย
            else:
                output_str = output_str + "\n"

        output_str = output_str + "     ]\n"
        output_str = output_str + "     :searchField=\"[ /* ค้นหาตาม column  อะไรได้บ้าง */ \n"

        for idx,col in enumerate(input_data):

            output_str = output_str + f"         '{col['field']}'"

            if idx != len(input_data)-1:
                output_str = output_str + ",\n"#ใส่ comma ถ้าไม่ใช่ตัวสุดท้าย
            else:
                output_str = output_str + "\n"

        output_str = output_str + "     ]\"\n"

        output_str = output_str + """ 
    :searchPlaceHolder="'searchAllColumn' /* place holder  ของ search text box */"
    :isMultiple="true /*กรณีเสิร์ชได้หลาย column */"
    :canResetSort="true"
/>"""

        #สำหรับ  Error
        output_str = output_str + "\n<!-- สำหรับตาราง แสดง Error -->\n"

        output_str = output_str + """
<DatatableForUpload
    ref="ErrorTableRef"
    :hideFilterText="false /* ซ่อนค้นหาตาม  text box หรือไม่ */"
    :tableStructure="[
    {
        header: 'percentCashCard.errorColumn',
        field: 'errorColumn',
        width: '25%',
        sortable: false,
    },
    {
        header: 'percentCashCard.errorMessage',
        field: 'errorMessage',
        width: '40%',
        sortable: false,
    },
    {
        header: 'percentCashCard.errorData',
        field: 'errorData',
        width: '39%',
        sortable: false,
    },
    ]"
    :searchField="[
    'errorColumn',
    'errorMessage',
    'errorData',
    ] /* ค้นหาตาม column  อะไรได้บ้าง */"
    :searchPlaceHolder="'searchAllColumn' /* place holder  ของ search text box */"
    :isMultiple="true /*กรณีเสิร์ชได้หลาย column */"
    :canResetSort="false"
    overflowX="hidden"
 />"""

        output_str = output_str + "\n<!--------------Script-------------->\n"

        output_str = output_str + """ 
const AcceptTableRef = ref();
const ErrorTableRef = ref();

const acceptData = ref({
  totalRow: 0,
  acceptDataList: [],
});
const errorData = ref({
  totalRow: 0,
  errorDataList: [],
});

const resetData = () => {
  acceptData.value = {
    totalRow: 0,
    acceptDataList: [],
  };

  errorData.value = {
    totalRow: 0,
    errorDataList: [],
  };
};

const setData = (data) => {
   
  //นำค่าใส่ข้อมูลที่ acceptData.value  กับ  errorData.value
  if (data) {
    acceptData.value.totalRow = data.totalRowAccept ? data.totalRowAccept : 0;
    errorData.value.totalRow = data.totalRowError ? data.totalRowError : 0;

    AcceptTableRef.value.reset(); //เพื่อให้  clear ข้อมูลใน table

    // acceptData.value = data;

    if (data.acceptDataList) {
      data.acceptDataList.forEach((el) => {
         .... /* จัด Format ข้อมูล */
      });
      AcceptTableRef.value.setData(data.acceptDataList);
    }
    if (data.errorDataList) {

      let errorData = [];
      data.errorDataList.forEach((el) => {
        const column = el.errorColumn.join(', ');
        errorData.push({
            ...el,
            errorData: `${{el.itemId}},${{el.effectiveStartDate}} ... `,
            errorColumn: column,
          });
      });
      ErrorTableRef.value.setData(errorData);
    }
  } else {
    resetData();
  }
};

const submitData = () => {
  let validate = true;
  if (acceptData.value.totalRow == 0) {
    validate = false;
  }
  return {
    validate: validate,
    data: AcceptTableRef.value.getData(),
  };
};

const resetTable = () => {
  acceptData.value = {
    totalRow: 0,
    acceptDataList: [],
  };
  errorData.value = {
    totalRow: 0,
    acceptDataList: [],
  };
  AcceptTableRef.value.reset();
  ErrorTableRef.value.reset();
};

defineExpose({
  setData,
  submitData,
  resetTable
});

"""

        output_field.value = output_str

        page.update()
    
    ### End function gen_out_put

    def open_dlg(row_data):

        #header
        header_txt_field = ft.TextField(label="header *",expand=True,value="")

        #field
        field_txt_field = ft.TextField(label="field *",expand=True,value="")

        #width
        width_txt_field = ft.TextField(label="width",expand=True,value="10% / 100px")

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
        
        if row_data is not None:
            #กรณีแก้ไข เอาข้อมูลเดิมมาใส่ในฟอร์ม
            header_txt_field.value = row_data['header']
            field_txt_field.value = row_data['field']
            width_txt_field.value = row_data['width']
            sortable_drop_down.value = row_data['sortable']
            align_drop_down.value = row_data['align']
        
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
                row_data['header'] = header_txt_field.value
                row_data['field'] = field_txt_field.value
                row_data['width'] = width_txt_field.value
                row_data['sortable'] = sortable_drop_down.value
                row_data['align'] = align_drop_down.value
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
    
    #ปุ่มเพิ่มแถว
    add_input_btn = ft.FilledButton(text="Add Column",icon=ft.Icons.ADD_OUTLINED,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=200,on_click=lambda e: open_dlg(None))
    #ปุ่มสร้าง code
    gen_btn = ft.FilledButton(text="Generate",icon=ft.Icons.CODE,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=200,on_click=gen_out_put)

    btn_row = ft.Row(controls=[add_input_btn, gen_btn])

    import_field = ft.TextField(label="Import",value=" ",expand=True,multiline=True,min_lines=2,border_color="blue")
    output_field = ft.TextField(label="Output",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue")


    def render_row_page():
        row_control.controls.clear()
        row_control.controls.append(row_1)

        if len(input_data) != 0: #สร้างหัวตาราง ถ้ามีข้อมูล
            row_control.controls.append(ft.Container(
                content=ft.Row(controls=[
                    ft.Text("Header", width=250,weight=ft.FontWeight.BOLD,color="BLUE"),
                    ft.Text("Field", width=250,weight=ft.FontWeight.BOLD,color="BLUE"),
                    ft.Text("Width", width=70,weight=ft.FontWeight.BOLD,color="BLUE"),
                    ft.Text("Sortable", width=70,weight=ft.FontWeight.BOLD,color="BLUE"),
                    ft.Text("Align", width=70,weight=ft.FontWeight.BOLD,color="BLUE"),
                    ft.Text("Action", width=50,weight=ft.FontWeight.BOLD,color="BLUE"),
                ],height=25),
            ))
            row_control.controls.append(ft.Divider())

        for idx, row_data in enumerate(input_data):

            row_control.controls.append(
                ft.Container(
                    content=ft.Row(controls=[
                        ft.Text(row_data['header'], width=250),
                        ft.Text(row_data['field'], width=250),
                        ft.Text(row_data['width'], width=70),
                        ft.Text(row_data['sortable'], width=70),
                        ft.Text(row_data['align'], width=70),
                        ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, rd=row_data: open_dlg(rd)),
                        ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, on_click=lambda e, i=idx: (input_data.pop(i), render_row_page()))
                    ],height=25),
                    # border=ft.border.all(1, ft.colors.BLACK),
                    # border_radius=ft.border_radius.all(6),
                    # padding=ft.padding.all(8),
                    # margin=ft.margin.symmetric(vertical=4)
                )
            )

            row_control.controls.append(ft.Divider())

        row_control.controls.append(btn_row)
        if len(input_data) > 0:
            #สร้างช่อง import output  ก็ต่อเมื่อมีข้อมูล
            row_control.controls.append(import_field)
            row_control.controls.append(output_field)

        page.update()

    row_control = ft.Column()
    render_row_page()

    return row_control