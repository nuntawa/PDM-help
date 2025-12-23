# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def Home(container,frames):
    # ---------- Home ----------
    home = ttk.Frame(container)
    home.grid(row=0, column=0, sticky="nsew")

    #----- เพิ่ม  widget  เข้าไปใน  Home
    ttk.Label(home, text="Home Page", font=("Arial", 18)).pack(pady=20)
    # ttk.Button(home, text="Go to Profile", command=lambda: show("profile")).pack()
    ttk.Button(home, text="Go to Profile", command=lambda: frames["profile"].tkraise() ).pack()

    return home