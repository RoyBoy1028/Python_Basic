from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title('MINSOO GUI')
window.geometry('640x480')
window.resizable(True, False)

# Menu Section
mymenu = Menu(window)
menu_file = Menu(mymenu, tearoff=0)


def create_new_menu():
    pass

menu_file.add_command(label="New File", command=create_new_menu)
menu_file.add_command(label="New Window", command=create_new_menu)
menu_file.add_separator()
menu_file.add_command(label="Open File", command=create_new_menu)
menu_file.add_command(label="Save File", command=create_new_menu)
menu_file.add_separator()
menu_file.add_command(label="Exit", command= window.quit)

mymenu.add_cascade(label="File", menu=menu_file)

window.config(menu=mymenu)
window.mainloop()