from tkinter import *
import tkinter.ttk as ttk
import os
from pathlib import Path
from tkinter import filedialog

file_name = '*.txt'

window = Tk()
window.title(f'Roy Notepad - {file_name}')
window.geometry('640x480')
window.resizable(True, True) 

# Menu Section
mymenu = Menu(window)
menu_file = Menu(mymenu, tearoff=0)

file_path = os.path.dirname(__file__)

def open_file():
    global file_name
    file_name = filedialog.askopenfilename(title="Select Text File", 
                                           filetypes=(('Text File', '*.txt'), ("All Files", "*.*")),
                                           initialdir=f"{file_path}")
    if os.path.isfile(file_name): 
        with open(file_name, 'r', newline='') as txt_file:
            txt_box.delete("1.0", END)
            txt_box.insert(END, txt_file.read())
    file_name = Path(file_name).stem
    window.title(f'Roy Notepad - {file_name}')

def browse_dest_path():
    file_save = filedialog.asksaveasfilename(title="Save",
                                             defaultextension= '.txt',
                                             filetypes=(('Text File', '*.txt'), ("All Files", "*.*")),
                                             initialdir=f"{file_path}")
    if file_save =="":      # Clicked cancel button
        return
    return file_save

def save_file():
    global file_name
    file_path = browse_dest_path()
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(txt_box.get("1.0", END))

    file_name = Path(file_name).stem
    window.title(f'Roy Notepad - {file_name}')

menu_file.add_command(label="Open File", command = open_file)
menu_file.add_command(label="Save File", command = save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command= window.quit)

mymenu.add_cascade(label="File", menu=menu_file)

#Scrollbar Section
scr = Scrollbar(window)
scr.pack(side="right", fill="y")

# Text Section
txt_box = Text(window, width=30, height=10, yscrollcommand=scr.set)       #width: numbers of letters // height : numbers of lines
txt_box.pack(fill="both", expand = True)
scr.config(command=txt_box.yview)

window.config(menu=mymenu)
window.mainloop()