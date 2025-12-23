# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pages.home import Home #แยกเป็นหน้าย่อย

# root = tk.Tk()
root = ttk.Window(themename="united")
root.geometry("600x500")

frames = {}

def show(route):
    frames[route].tkraise()

container = ttk.Frame(root)
# container.pack(fill="both", expand=True)
container.grid(row=1, column=0, sticky="nsew")

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

show("home")#แสดง frame  home เป็นอันแรก

#ให้อยู่บนสุดเสมอ
root.attributes('-topmost', True)

#แก้ size  ไม่ได้
root.resizable(False, False) 

root.mainloop()
