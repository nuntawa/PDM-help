import tkinter as tk

root = tk.Tk()
root.geometry("600x500")

frames = {}

def show(route):
    frames[route].tkraise()

container = tk.Frame(root)
# container.pack(fill="both", expand=True)
container.grid(row=1, column=0, sticky="nsew")

# ---------- Home ----------
home = tk.Frame(container)
home.grid(row=0, column=0, sticky="nsew")

#----- เพิ่ม  widget  เข้าไปใน  Home
tk.Label(home, text="Home Page", font=("Arial", 18)).pack(pady=20)
tk.Button(home, text="Go to Profile", command=lambda: show("profile")).pack()

# ---------- Profile ----------
profile = tk.Frame(container)
profile.grid(row=0, column=0, sticky="nsew")

#----- เพิ่ม  widget  เข้าไปใน  profile
tk.Label(profile, text="Profile Page", font=("Arial", 18)).pack(pady=20)
tk.Button(profile, text="Back to Home", command=lambda: show("home")).pack()

#----- ใส่ frame เข้าไปใน  dictionary
frames["home"] = home
frames["profile"] = profile

show("home")#แสดง frame  home เป็นอันแรก

#ให้อยู่บนสุดเสมอ
root.attributes('-topmost', True)
root.attributes('-topmost', False)

#แก้ size  ไม่ได้
root.resizable(False, False) 

root.mainloop()
