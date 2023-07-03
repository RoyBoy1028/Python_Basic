from tkinter import *
import webbrowser
import tkinter.messagebox as msgbox
import csv
import os

window = Tk()
window.title("ROY TOP 3 DIRECT LINK")
# window.geometry("320x480")

# Information Section (Frame, Label, variable)
title_frame = Frame(window, padx=10, pady=10)
title_frame.pack(fill='x')

title = '''
        [Top 3 Sites]
'''
label_var = Label(title_frame, text=title, padx=10, pady=10)
label_var.pack(side="top")
# Radio Buttons Section (Frame, Radio buttons - grid (pack x), variable) # .grid(row=n , column= m)
rdbt_frame = Frame(window, relief='solid', bd=1, padx=10, pady=10)
rdbt_frame.pack()

def link1():
     label = Label(lframe, text = "https://www.amazon.ca/")
def link2():
     label = Label(lframe, text = "https://www.amazon.ca/")
def link3():
     label = Label(lframe, text = "https://www.amazon.ca/")
def link4():
     label = Label(lframe, text = "https://www.amazon.ca/")

select_link = IntVar()
rdbt_amazon = Radiobutton(rdbt_frame, text = "Amazon", value=1, variable=select_link, command = link1)
rdbt_naver = Radiobutton(rdbt_frame, text = "Naver", value=2, variable=select_link, command = link2)
rdbt_google = Radiobutton(rdbt_frame, text = "Google", value=3, variable=select_link, command = link3)
rdbt_youtube = Radiobutton(rdbt_frame, text = "Youtube", value=4, variable=select_link, command = link4)

rdbt_amazon.grid(row=1, column=1, sticky='w')
rdbt_naver.grid(row=1, column=2, sticky='w')
rdbt_google.grid(row=2, column=1, sticky='w')
rdbt_youtube.grid(row=2, column=2, sticky='w')

# Link Path Section (Label Frame, Label(label text are random but do it if you can))
lframe = LabelFrame(window, text="Direct Link", padx=10, pady=10)
lframe.pack()
label = Label(lframe, text= "link")
label.pack()

# Open btn Section (Frame, two btn, def pass)
btn_frame = Frame(window, padx=10, pady=10)
btn_frame.pack()
open = Button(btn_frame, text="Open")
open.pack(side="left")
change = Button(btn_frame, text="Change Link")
change.pack(side="right")

# Save & Exit button (btn, command=quit)
save_close = Button(window, text="Save & Close", padx=10, pady=10)
save_close.pack(side="bottom")
## Tip
# webbrowser.open("target_url")

window.mainloop()