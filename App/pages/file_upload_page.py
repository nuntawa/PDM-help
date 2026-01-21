import flet as ft

def file_upload_page_render(page):

    def gen_out_put(e):
        if ref_text_field.value == "" or v_model_text_field.value == "" or uploader_text_field.value == "" or validateBeforeUpload_text_field.value == "" :
            page.show_error("Can not generate code","Please input all required element")
            return
        
        import_field.value = "import FileUpload from \"@/components/middle/CustomFileUpload/FileUploadPDMOnline\";"

        output_str = f"""<FileUpload
                    ref="{ref_text_field.value}"
                    v-model:fileValue="{v_model_text_field.value}"
                    @uploader="{uploader_text_field.value}"
                    :validateBeforeUpload="{validateBeforeUpload_text_field.value}"
                />

            <!-- Script -->
            const {ref_text_field.value} = ref();
            const {v_model_text_field.value} = ref();

            const checkFileExists = (file) => {{
                return new Promise((resolve, reject) => {{
                    if (typeof file.fileUrl != "string") {{
                    file.fileUrl = URL.createObjectURL(file);
                    }}

                    fetch(file.fileUrl)
                    .then((blobData) => {{
                        if (!blobData.ok) {{
                        reject({{ message: "File not found.", responseCode: "0500" }}); // Toast
                        }} else {{
                        resolve("Files Exists");
                        }}
                    }})
                    .catch(() => {{
                        reject({{ message: "File not found.", responseCode: "0500" }}); // Toast
                    }});
                }});
            }};
        """
        output_str =  output_str  + """const onClear = () => {
                """+v_model_text_field.value+""".value = null;
                """+ref_text_field.value+""".value.clear();
            };

            const """+uploader_text_field.value+""" = async(e)=>{

                try {
                    store.dispatch("startLoading");

                    await checkFileExists(e); // เช็คไฟล์โดนลบก่อนกดอัพโหลด

                    const data = {
                       //json ส่งข้อมูลให้  API
                       "companyId" : route.params.companyId,
                       "userId" :  sessionStorage.getItem("userId"),
                    };
                    // Call API
                    const resUpload = await Object.uploadMethod(e,data);

                    if (resUpload.responseCode === "0200") {
                        //แสดง  Toast  success
                        //props.showError?.showSuccess();

                    }

                    //ส่งข้อมูลมให้ตาราง แสดงผล
                    //props.TableUploadRef.setData(resUpload.result);

                } catch (error) {
                    props.showError(error);
                } finally {
                    """+ref_text_field.value+""".value.clear();
                    """+ref_text_field.value+""".value.uploadedFileCount = 0; // เพื่อให้สามารถอัพโหลดไฟล์ใหม่ได้
                    """+v_model_text_field.value+""".value = null;
                    store.dispatch("endLoading");
                }
            
            }

            defineExpose({
                onClear
            });
            
        """

        output_field.value = output_str

        page.update()
        

    row_1 = ft.Row(controls=[
        ft.Text("File Upload",size=15)
    ])

    ref_text_field = ft.TextField(label="ref *",value="UploadRef")
    v_model_text_field = ft.TextField(label="v-model:fileValue *",value="currentFile")
    uploader_text_field = ft.TextField(label="@uploader *",value="onUpload")#ชื่อ Function ที่ทำงานเมื่อ  upload
    validateBeforeUpload_text_field = ft.TextField(label="validateBeforeUploa *",value="...เงื่อนไข ปุ่ม upload enabled... ? true : false")

    row_2 = ft.Row(controls=[
        ref_text_field,v_model_text_field,uploader_text_field,validateBeforeUpload_text_field
    ])

    gen_btn = ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    row_3 = ft.Row(controls=[gen_btn])

    import_field = ft.TextField(label="Import",value=" ",min_lines=2,border_color="blue",multiline=True,
                                    expand=True,#ยาวเต็ม 100%
    )
    row_4 = ft.Row(controls=[import_field])

    output_field = ft.TextField(label="Code",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue") 
    row_5 = ft.Row(controls=[output_field])

    row_control = ft.Column(controls=[
        row_1,row_2,row_3,row_4,row_5
    ])   

    return row_control