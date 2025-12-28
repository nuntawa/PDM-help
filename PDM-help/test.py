import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x150')

options = ['Option A', 'Option B', 'Option C']

# Create the Combobox
# The 'values' argument sets the available options in the dropdown list
combo_box = ttk.Combobox(root, values=options)
combo_box.pack(pady=20)

# Set the default value to 'Option B'
combo_box.set('Option B')

root.mainloop()