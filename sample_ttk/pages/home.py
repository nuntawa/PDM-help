# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.scrolled import ScrolledFrame

def Home(container,frames):
    # ---------- Home ----------
    # page = ttk.Frame(container)
    page = ttk.Frame(container)
    page.grid(row=0, column=0, sticky="nsew")
    #Responsive layout
    page.grid_columnconfigure(0, weight=1)
    page.grid_columnconfigure(1, weight=1)
    page.grid_rowconfigure(2, weight=1)

    # sf = ScrolledFrame(page,autohide=True)
    # sf.grid(row=0, column=0,columnspan=12, sticky="nsew")
    # sf.pack(fill=BOTH, expand=YES)

    #----- เพิ่ม  widget  เข้าไปใน  Home
    home_label = ttk.Label(page, text="Home Page", font=("Arial", 10))
    home_label.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
    home_label2 = ttk.Label(page, text="Home Page", font=("Arial", 10))
    home_label2.grid(row=0,column=1,padx=5,pady=5,sticky="nsew")

    change_page_btn = ttk.Button(page, text="Go to Profile", command=lambda: frames["profile"].tkraise() )
    change_page_btn.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")
    
    # text_area = ttk.Text(page,height=180,width=129)
    # text_area.grid(row=2,column=0,columnspan=12,padx=5,pady=5,sticky="NEWS")

    st = ScrolledText(page, autohide=True)
    st.grid(row=2,column=0,columnspan=4,padx=5,pady=5,sticky="nsew")
    st.insert(END, 'Insert your text here.')

    clear_btn = ttk.Button(page, text="Clear Text", command=lambda: st.delete('1.0', END) , takefocus=False , bootstyle=PRIMARY )
    clear_btn.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")

    return page