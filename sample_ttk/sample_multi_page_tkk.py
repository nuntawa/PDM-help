# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pages.home import Home #แยกเป็นหน้าย่อย
from ttkbootstrap.scrolled import ScrolledFrame

# root = tk.Tk()
root = ttk.Window(title="PDM Help",themename="united")
root.geometry("900x650")
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)

#เมนู bar
menu_bar = ttk.Menu(root)

#Group ของเมนู
layout_menu = ttk.Menu(menu_bar,tearoff=0)
layout_menu.add_command(label = "หน้าแม่",command=lambda:print("หน้าแม่"))
layout_menu.add_command(label = "Tab มี Card",command=lambda:print("Tab มี card"))
layout_menu.add_command(label = "Card มี Tab",command=lambda:print("Card มี Tab"))

#component เมนู
component_menu = ttk.Menu(menu_bar,tearoff=0)
component_menu.add_command(label = "grid",command=lambda:print("grid"))
component_menu.add_command(label = "dropdown",command=lambda:print("dropdown"))
component_menu.add_command(label = "button",command=lambda:print("button"))

#เพิ่มเข้าไปในเมนู bar  ด้านบน
menu_bar.add_cascade(label="Layout",menu=layout_menu)
menu_bar.add_cascade(label="component",menu=component_menu)

root.config(menu=menu_bar)

frames = {}

def show(route):
    frames[route].tkraise()

container = ttk.Frame(root)
container.pack(fill="both", expand=True)
# container = ScrolledFrame(root,autohide=True)
# container.pack(fill="both", expand=True)
# container.grid(row=0, column=0, sticky="nsew")
# container.pack(fill="both", expand=True)
 #Responsive layout
# container.grid_columnconfigure(0, weight=1)
# container.grid_rowconfigure(0, weight=1)

# # ---------- Home ----------
# home = ttk.Frame(container)
# home.grid(row=0, column=0, sticky="nsew")

# #----- เพิ่ม  widget  เข้าไปใน  Home
# ttk.Label(home, text="Home Page", font=("Arial", 18)).pack(pady=20)
# ttk.Button(home, text="Go to Profile", command=lambda: show("profile")).pack()
home = Home(container,frames)


# ---------- Profile ----------
profile = ttk.Frame(container)
profile.grid(row=0, column=0, sticky="nsew")

#----- เพิ่ม  widget  เข้าไปใน  profile
ttk.Label(profile, text="Profile Page", font=("Arial", 18)).pack(pady=20)
ttk.Button(profile, text="Back to Home", command=lambda: show("home")).pack()

#----- ใส่ frame เข้าไปใน  dictionary
frames["home"] = home
frames["profile"] = profile

show("profile")#แสดง frame  home เป็นอันแรก

#ให้อยู่บนสุดเสมอ
root.attributes('-topmost', True)

#แก้ size  ไม่ได้
root.resizable(False, False) 

root.mainloop()
