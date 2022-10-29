import tkinter as tk
from tkinter import ttk

from matplotlib.pyplot import text

def greet():
    print("Hello, WORLD")

root = tk.Tk()

greet_button = ttk.Button(root,text="Greet",command=greet)
greet_button.pack(side="left",fill="y") # pack() is used to put the item in window
# expand = True -> expand along with the window
# fill = both -> fill in both directions

quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack(side="left") #side="top"(default) # side is used for alignment

root.mainloop()

