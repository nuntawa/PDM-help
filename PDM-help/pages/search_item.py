import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from ttkbootstrap.scrolled import ScrolledText

def SearchItem(container,frames):
    page = ttk.Frame(container)
    page.columnconfigure(0,weight=1) 
    page.columnconfigure(1,weight=1) 
    page.columnconfigure(2,weight=1) 
    page.columnconfigure(3,weight=1) 
    
    page.rowconfigure(0,weight=1) 
    page.rowconfigure(1,weight=1) 
    page.rowconfigure(2,weight=1) 
    page.rowconfigure(3,weight=1) 
    page.rowconfigure(4,weight=1) 
    page.grid(row=0,column=0)

    ttk.Label(page,text="Label",bootstyle="primary",font=("Arial", 12)).grid(row=0,column=0,sticky="nw",padx=10,pady=10)
    label_txt = ttk.Entry(page)
    label_txt.grid(row=0,column=0,sticky="new",padx=10,pady=35)
    label_txt.delete(0,END)
    label_txt.insert(END,"ItemBasic.itemId")

    ttk.Label(page,text="v-model",bootstyle="primary",font=("Arial", 12)).grid(row=0,column=1,sticky="nw",padx=10,pady=10)
    v_modell_txt = ttk.Entry(page)
    v_modell_txt.grid(row=0,column=1,sticky="new",padx=10,pady=35)
    v_modell_txt.delete(0, END) 
    v_modell_txt.insert(END, 'itemObj')

    ttk.Label(page,text="ref",bootstyle="primary",font=("Arial", 12)).grid(row=0,column=2,sticky="nw",padx=10,pady=10)
    ref_txt = ttk.Entry(page)
    ref_txt.grid(row=0,column=2,sticky="new",padx=10,pady=35)
    ref_txt.delete(0,END)
    ref_txt.insert(END,"SearchItemRef")
    
    ttk.Label(page,text="isRequired",bootstyle="primary",font=("Arial", 12)).grid(row=0,column=3,sticky="nw",padx=10,pady=10)
    is_required_select = ttk.Combobox(page)
    is_required_select["values"] = ["true","false"]
    is_required_select.grid(row=0,column=3,sticky="new",padx=10,pady=35)
    is_required_select.bind("<<ComboboxSelected>>", lambda e :is_required_select.selection_clear())
    is_required_select.set("true")

    ttk.Label(page,text="isUserPermission",bootstyle="primary",font=("Arial",12)).grid(row=1,column=0,sticky="nw",padx=10,pady=10)
    is_user_permission_select = ttk.Combobox(page)
    is_user_permission_select["values"] = ["true","false"]
    is_user_permission_select.grid(row=1,column=0,sticky="new",padx=10,pady=35)
    is_user_permission_select.bind("<<ComboboxSelected>>", lambda e :is_user_permission_select.selection_clear())
    is_user_permission_select.set("true")

    ttk.Label(page,text="companyId",bootstyle="primary",font=("Arial",12)).grid(row=1,column=1,sticky="new",padx=10,pady=10)
    company_id_txt = ttk.Entry(page)
    company_id_txt.grid(row=1,column=1,sticky="new",padx=10,pady=35)
    company_id_txt.delete(0,END)
    company_id_txt.insert(END,"route.params.companyId")

    gen_btn = ttk.Button(page,text="Generate Code",takefocus=False,bootstyle=PRIMARY,command= lambda: print('Generate Code'))
    gen_btn.grid(row=1,column=2,sticky="new",padx=10,pady=35)

    # ttk.Label(page,text="Import",bootstyle="primary",font=("Arial",12)).grid(row=2,column=0,sticky="nw",padx=10,pady=10)
    # import_txt_area = ScrolledText(page, autohide=True)
    # import_txt_area.delete('0.0', END)
    # import_txt_area.insert(END, '')#เพิ่มข้อความเข้าไปใน Scrool text area
    # import_txt_area.grid(row=2,column=0,columnspan=4,padx=5,pady=5,sticky="sew")

    ttk.Label(page,text="Code",bootstyle="primary",font=("Arial",12)).grid(row=3,column=0,sticky="nw",padx=10,pady=10)    
    code = ScrolledText(page, autohide=True)
    code.delete('0.0', END)
    code.insert(END, '')#เพิ่มข้อความเข้าไปใน Scrool text area
    code.grid(row=3,column=0,rowspan=2,columnspan=4,padx=5,pady=5,sticky="sew")

    return page
    