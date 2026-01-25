import flet as ft

def mother_page_render(page):

    def gen_out_put(e):
        if program_code_field.value =="" or program_name_field.value == "":
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
        
        tab_import_str = ""
        card_import_str = ""
        tab_content_str = ""
        card_content_str = ""
        tab_script_str = ""

        if content_dropdown.value == "tab":

            tab_import_str = """import Card from "primevue/card";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";"""
            tab_content_str = """  <div class="blue-tab-container">

                <TabView :activeIndex="activeIndex" @tab-click="typeSwitch">
                    <TabPanel :header="t('...')">
                        <Card  class="pdm-box" >
                            <template #content>
                                
                            </template>
                        </Card>
                    </TabPanel>
                    <TabPanel :header="t('...')">
                        <Card   class="pdm-box" >
                            <template #content>
                                
                            </template>
                        </Card>
                    </TabPanel>
                </TabView>
                    

</div> """
            tab_script_str = """
const activeIndex = ref(0);
const typeSwitch = (event) => {
  activeIndex.value = event.index;
};
"""

        elif content_dropdown.value == "card":
            card_import_str = "import Card from \"primevue/card\"; "
            card_content_str = """<Card class="pdm-box">
        <template #content>
            
        </template>
</Card>"""


        output_str="""<template>
    <div>

        <ShowErrorOrSuccess
                ref="ShowErrorOrSuccessRef"
        />

        <HeaderCompany
            ref="HeaderCompanyRef"
            :programType="programType"
            :programName="programName"
            :method="''"
            :programCode="programCode"
            :lostCompanyResponseCode="''"
            :onFnishLoading="
                null /*()=>store.dispatch('endLoading') HeaderCompany  จะไม่ stoploading ต้้องใส่ onFnishLoading เอง ( ถ้ามีข้อมูลที่ต้องดึงจาก api สามารถกำหนด onFnishLoading  เป็น null ได้  )*/
            "
            :showError="(error) => ShowErrorOrSuccessRef.showError(error)"
            :notFoundMessage="'' /* ข้อความที่ต้องการให้แสดงถ้าไม่พบ compnay เพราะในหน้า  form  จะเป็น error  เรื่องสิทธิ ( ถ้าเป็นค่าว่างจะยึดตาม error ( responseCode , responseMessage ) ของ getCompanyInfo  ) */"
            />
            """+tab_content_str+"""
            """+card_content_str+"""

        <!--<หน้าลูก
                  ref="ชื่อref"
                  v-if="dataFromAPI"
                  :dataFromAPI="dataFromAPI"
                  :showError="showError"
                  :showSuccess="showSuccess"
        />-->

    </div>
</template>
<script setup>
import { useStore } from 'vuex';
import { ref ,onMounted, watch, computed} from "vue";
import { useI18n } from 'vue-i18n';
import HeaderCompany from '@/components/middle/HeaderCompany/header-company.vue';
import showErrorOrSuccess from '@/components/middle/ShowErrorOrSuccess/showError-or-success.vue';
import { useRoute,useRouter } from 'vue-router';
import SettingService from '@/services/setting-service';
import ShowErrorOrSuccess from '@/components/middle/ShowErrorOrSuccess/showError-or-success.vue';
"""+tab_import_str+"""
"""+card_import_str+"""

const router = useRouter();

const ShowErrorOrSuccessRef = ref();
const HeaderCompanyRef = ref();
const store = useStore();
const route = useRoute();
const { t } = useI18n();

const programCode = ref(\""""+program_code_field.value+"""\");
const programType = ref(\""""+module_dropdown.value+"""\");
const programName = ref(\""""+program_name_field.value+"""\");

const dataFromAPI = ref(null);

"""+tab_script_str+"""

const permissionAdd = ref(
  // SettingService.checkActionProgram(program.value, "CREATE")
  SettingService.checkActionProgram(programCode.value, "EDIT")
);
const permissionView = ref(
  SettingService.checkActionProgram(programCode.value, "VIEW")
);
const permissionEdit = ref(
  SettingService.checkActionProgram(programCode.value, "EDIT")
);
const permissionDelete = ref(
  SettingService.checkActionProgram(programCode.value, "DELETE")
);



const showError = ref((error) => {
  // สำหรับ แสดง Error ส่งให้หน้าลูก
  if (store.state.loading) {
    store.dispatch("endLoading");
  }

  ShowErrorOrSuccessRef.value.showError(error);
  
});

const showSuccess = ref(() => {
  // สำหรับ แสดง Error ส่งให้หน้าลูก
  if (store.state.loading) {
    store.dispatch("endLoading");
  }

    
  ShowErrorOrSuccessRef.value.showSuccess();
  
});

onMounted(async ()=>{

    if (
        !permissionAdd.value &&
        !permissionView.value &&
        !permissionEdit.value &&
        !permissionDelete.value
    ) {
        store.dispatch("setPermissionActionFlag", "2"); //ไม่ไปหน้าไหนเลย
        store.dispatch("noPermissionAction");
    }

    let headerCompanySuccessInit = await HeaderCompanyRef.value.init();
    if (!headerCompanySuccessInit) {
        //company  หาย ......... ????
        return;
    }

    await fetchData();
});

const fetchData = async ()=>{

    try {

        // let [res] = await Promise.all([
        //     callAPIService,
        // ]);

        // if(res.responseCode != "0200")
        // {
        //     throw({
        //         responseCode:res.responseCode,
        //         message:res.responseMessage
        //     });
        // }

        // res.result?.forEach((i) => {
        //     i.name = i.codeValue + " : " + i.codeName;
        //     i.value = i.codeValue;
        // });

        // dataFromAPI.value = {
        //     crossdockFlg:res.result,
        //     ...
        // };
        
    } catch (error) {
        store.dispatch("endLoading");
        ShowErrorOrSuccessRef.value.showError(error);
    }
    store.dispatch("endLoading");
}

</script>"""
        output_field.value = output_str
        page.update()


    program_code_field = ft.TextField(label="Program Code * ",value="",hint_text="PI101")
    program_name_field = ft.TextField(label="Program Name *",value="",hint_text="Item Basic")
    module_dropdown = ft.Dropdown(label="Module *",options=[
        ft.dropdown.Option(text="Product Information",key="Product Information"),
        ft.dropdown.Option(text="Reports",key="Reports"),
        ft.dropdown.Option(text="Master Information",key="Master Information")
    ],value="Product Information")

    gen_btn = ft.FilledButton(text="Generate",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=gen_out_put)

    #Text Field ที่แสดง code output
    output_field = ft.TextField(label="Code",value=" ",expand=True,multiline=True,min_lines=10,border_color="blue")

    content_dropdown = ft.Dropdown(label="Content Type",options=[
        ft.dropdown.Option(text="Tab",key="tab"),
        ft.dropdown.Option(text="Card",key="card"),
        ft.dropdown.Option(text="None",key="none")
    ],value="tab")

    row_1 = ft.Row(controls=[ft.Text("หน้าแม่",size=15)])
    row_2 = ft.Row(controls=[program_code_field,program_name_field,module_dropdown,content_dropdown,gen_btn])
    row_3 = ft.Row(controls=[])
    row_4 = ft.Row(controls=[output_field])

    row_control = ft.Column(controls=[
        row_1,
        row_2,
        row_4
         
    ])

    return row_control