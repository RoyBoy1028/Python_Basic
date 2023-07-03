from tkinter import *
import tkinter.ttk as ttk
import os
from PIL import Image


window = Tk()
window.title("ROY IMAGE FUSION")

#File btn frame
file_frame = Frame(window)
file_frame.pack(fill='x', padx = 5, pady = 5)

def add_file():
    pass

btn_add_file = Button(file_frame, text ="Add Files", command=add_file)
btn_add_file.pack(side='left', padx = 5, pady = 5)

def del_file():
    pass

btn_del_file = Button(file_frame, text ="Delete Files", command=del_file)
btn_del_file.pack(side='right', padx = 5, pady = 5)

# List Frame
list_frame = Frame(window)
list_frame.pack(fill='both', padx=5, pady=5)

#Scrollbar Section
scr = Scrollbar(list_frame)
scr.pack(side="right", fill="y")

# List Section
list_box = Listbox(list_frame, selectmode="extended",height=15, yscrollcommand=scr.set)       #width: numbers of letters // height : numbers of lines
list_box.pack(side="left", fill="both", expand = True)
scr.config(command=list_box.yview)

# Save path Frame
path_frame = LabelFrame(window, text="Save Path")
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

dest_path = Entry(path_frame)
dest_path.pack(side="left", fill='x', expand=True, padx=5, pady=5, ipady=4)

def browse_dest_path():
    pass

btn_dest_path = Button(path_frame, text="Browse..", width=10, command=browse_dest_path)
btn_dest_path.pack(side='right', padx=5, pady=5)

# Option Frame
opt_frame = LabelFrame(window, text="Option")
opt_frame.pack(fill='x', padx=5, pady=5, ipady=5)

# 1. Width
width_lab = Label(opt_frame, text="width (px)", width = 8)
width_lab.pack(side="left", padx=5, pady=5)

width_val = ['Original', '1024', '800', '640']
cmb_width = ttk.Combobox(opt_frame, values=width_val, state="readonly", width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. Extention
ext_lab = Label(opt_frame, text="Format", width = 8)
ext_lab.pack(side="left", padx=5, pady=5)

ext_val = ['JPG', 'PNG', 'BMP']
cmb_ext = ttk.Combobox(opt_frame, values=ext_val, state="readonly", width=10)
cmb_ext.current(0)
cmb_ext.pack(side="left", padx=5, pady=5)

# 3. Spacing
space_lab = Label(opt_frame, text="Spacing", width = 8)
space_lab.pack(side="left", padx=5, pady=5)

space_val = ['None', 'Slim', 'Normal', 'Wide']
cmb_space = ttk.Combobox(opt_frame, values=space_val, state="readonly", width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# Progress Bar
p_frame = LabelFrame(window, text="Progress state")
p_frame.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(p_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Buttons
run_frame = Frame(window)
run_frame.pack(fill='x', padx=5, pady=5, ipady=5)

btn_close = Button(run_frame, padx=5, pady=5, text ="Close", command=window.quit)
btn_close.pack(side='right', padx = 5, pady = 5)

def fusion_image():
    pass

btn_start = Button(run_frame, padx=5, pady=5,text ="Start", command=fusion_image)
btn_start.pack(side='right', padx = 5, pady = 5)

window.mainloop()