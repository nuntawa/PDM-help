import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from tkinter import PhotoImage
from pages.home import Home #แยกเป็นหน้าย่อย
from pages.search_item import SearchItem #แยกเป็นหน้าย่อย


root = ttk.Window(title="PDM Help",themename="united")
root.geometry("900x650")

frames = {}

def show(route):
    frames[route].tkraise()

#เมนู bar
menu_bar = ttk.Menu(root)

#Group ของเมนู
layout_menu = ttk.Menu(menu_bar,tearoff=0)
layout_menu.add_command(label = "หน้าแม่",command=lambda:show("home"))
layout_menu.add_command(label = "Tab มี Card",command=lambda:print("Tab มี card"))
layout_menu.add_command(label = "Card มี Tab",command=lambda:print("Card มี Tab"))

#component เมนู
component_menu = ttk.Menu(menu_bar,tearoff=0)
component_menu.add_command(label = "grid",command=lambda:print("grid"))
component_menu.add_command(label = "dropdown",command=lambda:print("dropdown"))
component_menu.add_command(label = "button",command=lambda:print("button"))
component_menu.add_command(label = "Search Item",command=lambda:show("search_item"))


#เพิ่มเข้าไปในเมนู bar  ด้านบน
menu_bar.add_cascade(label="Layout",menu=layout_menu)
menu_bar.add_cascade(label="component",menu=component_menu)

root.config(menu=menu_bar)
 
container = ttk.Frame(root)
container.pack(fill="both", expand=True)
container.columnconfigure(0,weight=1)
container.rowconfigure(0,weight=1)
container.grid_propagate(False)

# container.grid(row=0,column=0,sticky="nsew")
# home = Home(container,frames)
# search_item = SearchItem(container,frames)

frames["home"] = Home(container,frames)
frames["search_item"] = SearchItem(container,frames)

for frame in frames.values():
    frame.grid(row=0, column=0, sticky="nsew")

show("home")


# frame = ttk.Frame(root)

# frame.columnconfigure(0,weight=1)#ประกาศ grid column 0
# # frame.columnconfigure(1,weight=1)#ประกาศ grid column 1
# frame.rowconfigure(0,weight=1)#ประกาศ row column 1
# # frame.rowconfigure(1,weight=1)#ประกาศ row column 1
# frame.pack(fill="both", expand=True)

# img = PhotoImage(file="pdm_icon.ico")
# label = ttk.Label(frame, image=img)
# label.image = img
# label.grid(row=0,column=0)

# ttk.Label(frame, text="Home", font=("Arial", 12),background="green").grid(row=0,column=0)
# ttk.Label(frame, text="Home2", font=("Arial", 12),background="blue").grid(row=0,column=1)

# st = ScrolledText(frame, autohide=True)
# st.insert(END, 'Insert your text here.')
# st.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")



#ให้อยู่บนสุดเสมอ
root.attributes('-topmost', True)

#แก้ size  ไม่ได้
root.resizable(False, False) 

root.mainloop()