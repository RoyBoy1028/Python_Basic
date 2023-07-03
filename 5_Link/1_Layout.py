from tkinter import *
import webbrowser
import tkinter.messagebox as msgbox
import csv
import os

save_path = os.path.dirname(__file__)

with open(f"{save_path}/save.csv", 'r') as read_file:
     reader = csv.reader(read_file)
     for row in reader:
          links = row

read_file.close()

target_url = links[0]
now_url = target_url

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

def path_change():
     global target_url
     global now_url

     now_url = links[select_link.get()]

     label.config(text=now_url)
     target_url = now_url

select_link = IntVar()
rdbt_amazon = Radiobutton(rdbt_frame, text = "Amazon", value=0, variable=select_link, command = path_change)
rdbt_naver = Radiobutton(rdbt_frame, text = "Naver", value=1, variable=select_link, command = path_change)
rdbt_google = Radiobutton(rdbt_frame, text = "Google", value=2, variable=select_link, command = path_change)
rdbt_youtube = Radiobutton(rdbt_frame, text = "Youtube", value=3, variable=select_link, command = path_change)

rdbt_amazon.grid(row=1, column=1, sticky='w')
rdbt_naver.grid(row=1, column=2, sticky='w')
rdbt_google.grid(row=2, column=1, sticky='w')
rdbt_youtube.grid(row=2, column=2, sticky='w')

# Link Path Section (Label Frame, Label(label text are random but do it if you can))
lframe = LabelFrame(window, text="Direct Link", padx=10, pady=10)
lframe.pack()
label = Label(lframe, text= links[0])
label.pack()

# Open btn Section (Frame, two btn, def pass)
btn_frame = Frame(window, padx=10, pady=10)
btn_frame.pack()

def open_web():
     global target_url
     webbrowser.open(target_url)

def change():
     sub_win = Toplevel(window)
     sub_win.title("Change link as...")
     sub_win.geometry("300x100")

     e_frame = Frame(sub_win, padx=5, pady=5)
     e_frame.pack()

     e = Entry(e_frame)
     e.pack()
     e.insert(0, now_url)

     sub_btn_f = Frame(sub_win, padx=5, pady=5)
     sub_btn_f.pack()

     def apply():
          global target_url
          global now_url
          global links

          links[select_link.get()] = e.get()
          now_url = links[select_link.get()]
          target_url = now_url
          label.config(text=now_url)

          msgbox.showinfo("Notice", "Link is changed successfully!")

          e.delete(0, END)
          e.insert(0, now_url)

     btn_apply = Button(sub_btn_f, text="Apply", command = apply)
     btn_apply.pack(side="right", padx=5, pady=5)
     
     btn_done = Button(sub_btn_f, text="Done", command=sub_win.withdraw)
     btn_done.pack(side="right", padx=5, pady=5)


open_w = Button(btn_frame, text="Open", command=open_web)
open_w.pack(side="left")
change = Button(btn_frame, text="Change Link", command = change)
change.pack(side="right")

def save_exit(): 
     global save_path

     # Save 
     with open(f"{save_path}/save.csv", "w", newline='') as file:
          linklist = csv.writer(file)
          linklist.writerow(links)
     file.close()

     # Exit
     window.quit()
# Save & Exit button (btn, command=quit)
save_close = Button(window, text="Save & Close", padx=10, pady=10, command=save_exit)
save_close.pack(side="bottom")
## Tip
# webbrowser.open("target_url")

window.mainloop()