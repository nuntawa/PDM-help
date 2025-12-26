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
    page.grid(row=0,column=0)

    
    ttk.Label(page,text="v-model",bootstyle="primary",font=("Arial", 12)).grid(row=0,column=0,sticky="nw",padx=10,pady=10)
    ttk.Entry(page).grid(row=0,column=0,sticky="new",padx=10,pady=35)

    ttk.Label(page,text="ref",bootstyle="primary",font=("Arial", 12)).grid(row=0,column=1,sticky="nw",padx=10,pady=10)
    ttk.Entry(page).grid(row=0,column=1,sticky="new",padx=10,pady=35)
    

    st = ScrolledText(page, autohide=True)
    st.insert(END, 'Insert your text here.')
    st.grid(row=2,column=0,columnspan=5,rowspan=2,padx=5,pady=5,sticky="nsew")

    return page
    