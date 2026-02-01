import flet as ft

def button_page_render(page):

    def gen_out_put(e):

        selected_type = []
        for cb in checkboxes:
            if cb.value:
                selected_type.append(cb.key)
        

        import_field.value = "" #เคลียร์ค่าเดิมก่อน
        import_field.value = import_field.value + "import BlueThemButton from \"@/components/middle/BlueThemButton/BlueThemButton.vue\";\n"

        if "Delete" in selected_type:#กรณีเลือกปุ่ม Delete
            import_field.value =  import_field.value + "import ConfirmDelete from \"@/components/middle/DeleteDialog/ConfirmDelete.vue\";"
        
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
            elif btn_type !="Delete":
                output_str = output_str + f"    <BlueThemButton\n"
                output_str = output_str + f"         :buttonText=\"'"+btn_type+"'\"\n"

                if btn_type == "Search" or btn_type == "Add" or btn_type == "Set" :
                    output_str = output_str + f"     :cssButton=\"'bg-blue'\"\n"
                if btn_type == "Clear" or btn_type == "Back" :
                    output_str = output_str + f"     :cssButton=\"'font-black'\"\n"
                if btn_type == "Save"  :
                    output_str = output_str + f"     :cssButton=\"'bg-green'\"\n"
                    output_str = output_str + f"     :disabled=\"!permissionEdit\"\n"    
                if btn_type == "Report" :
                    output_str = output_str + f"     :cssButton=\"'bg-back'\"\n"
                    #output_str = output_str + f"     :disabled=\"!permissionReport\"\n"
                if btn_type == "Generate" :
                    output_str = output_str + f"     :cssButton=\"'bg-back'\"\n"
                    output_str = output_str + f"     :disabled=\"!permissionEdit /*กลุ่ม  Report  ไม่ต้องมี เช็คสิทธิ ( สิทธิ view ) */\"\n"
                    # พี่ทีบอก นาทีที่ 3:01 https://cpallgroup-my.sharepoint.com/personal/sudjaij_gosoft_co_th/_layouts/15/stream.aspx?id=%2Fpersonal%2Fsudjaij%5Fgosoft%5Fco%5Fth%2FDocuments%2FRecordings%2FPDM%20TeamB%2D20260122%5F135254%2DMeeting%20Recording%201%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E417b8c01%2D17c4%2D4d95%2Da58c%2D4ce16c733912&startedResponseCatch=true
                
                output_str = output_str + f"         :onClick=\"()=>{{ ... }}\"\n"
                output_str = output_str + f"         :styleInline=\"''\"\n"
                output_str = output_str + f"    />\n\n"
            else: #กรณีปุ่ม Delete
                output_str = output_str + f"    <ConfirmDelete\n"
                output_str = output_str + f"         v-model:visible=\"visibleConfirmDelete\"\n"
                output_str = output_str + f"         :visible=\"visibleConfirmDelete\"\n"
                output_str = output_str + f"         :onClick=\"openDialogDelete\"\n"
                output_str = output_str + f"         @openDialog=\"openDialogDelete\"\n"
                output_str = output_str + f"         @confirm=\"handleConfirmDelete\"\n"
                output_str = output_str + f"         :disabled=\"'!permissionDelete'\"\n"
                output_str = output_str + f"    />\n\n"
        #end for

        if content_end:
            output_str = output_str + f"</div>\n"

        if "Delete" in selected_type:
            output_str = output_str + "<-----Script ------->\n"
            output_str = output_str + "const visibleConfirmDelete = ref(false);/*  ปิด เปิด  popup  confirm ลบ */\n"
            output_str = output_str + """const openDialogDelete = () => {  

                /* validate  ก่อน  เปิด  popup  */
            
                visibleConfirmDelete.value = true; 

            }\n  """
            output_str = output_str + """const handleConfirmDelete = async (confirm) => { 

                try {
    
    if (confirm) {
        store.dispatch("startLoading");
      
        /*const res = await ObjAPI.เรียก API  delete(req);

        if (res.responseCode !== "0200") {
          throw {
            message: res.responseMessage,
            responseCode: res.responseCode,
          };
        }*/

        store.dispatch("endLoading");
        props.showSuccess();
     
    }
   
  } catch (error) {
    store.dispatch("endLoading");
    props.showError({
      message: error.message,
      responseCode: error.responseCode,
    });
  }

            }\n  """

        output_field.value = output_str
        page.update()

    row_1 = ft.Row(controls=[
        ft.Text("Button",size=15)
    ])

    #ตัวเลือกประเภทปุ่ม
    options = [
        ("ปุ่มด้านล่าง", "content-end"),
        ("Search", "Search"),
        ("Save", "Save"),
        ("Add", "Add"),
        ("Set", "Set"),
        ("Delete", "Delete"), #(ไปใช้  confirm  delete)
        ("Clear", "Clear"),
        ("Report", "Report"),
        ("Generate", "Generate"),
        ("Back", "Back"),
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