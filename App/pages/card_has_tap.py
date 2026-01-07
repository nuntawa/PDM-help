import flet as ft

def card_has_tab_render(page):

    row_1 = ft.Row(controls=[ft.Text("Card มี Tab",size=15)])

    text_field_arr = [
        ft.TextField(label="Tab name",width=800,value="`Accept Data (${acceptData?.totalRow?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')})`"),
        ft.TextField(label="Tab name",width=800,value="`Error Data (${errorData?.totalRow?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')})`")
    ]

    # build rows dynamically from text_field_arr so indices remain correct after removals
    def remove_row(row_num):
        print(row_num)
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
        page.update()
    
    ##end render_row_page

    add_input_btn = ft.FilledButton(text="Add Tab",icon=ft.Icons.ADD_OUTLINED,style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
    ),width=100,on_click=add_input_row)


    row_btn = ft.Row(controls=[add_input_btn])
    row_control = ft.Column()
    render_row_page()
    # row_control = ft.Column(
    #     controls=[
    #         row_1,row_btn
    #     ]
    # )

    return row_control