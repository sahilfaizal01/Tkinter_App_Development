import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello,{user_name.get() or 'World'}!")

root = tk.Tk()
user_name = tk.StringVar()

name_label = ttk.Label(root,text="Name: ")
name_label.pack(side="left", padx=(0,10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus() #to write right away when application starts

greet_button = ttk.Button(root,text="Greet",command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack(side="right") 

root.mainloop()

