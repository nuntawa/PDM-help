import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

def Home(container,frames):
    page = ttk.Frame(container)
    # page.pack(fill="both",expand=True)
    page.columnconfigure(0,weight=1) 
    page.rowconfigure(0,weight=1) 
    page.grid(row=0,column=0)

    img = PhotoImage(file="pdm_icon.ico")
    label = ttk.Label(page, image=img)
    label.image = img
    label.grid(row=0,column=0)
    return page