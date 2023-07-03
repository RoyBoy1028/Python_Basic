from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title('MINSOO GUI')
window.geometry('640x480')
window.resizable(True, False)

title = '''
        [Convert textbox to Label]
'''
label_var = Label(window, text=title)
label_var.pack(side="top")

def convert_t2label():
    change = txt_box.get("1.0", END)
    label_var.config(text=change)
    txt_box.delete("1.0", END)

# Button Section
btn1 = Button(window, text="Convert", command=convert_t2label)
btn1.pack(side="bottom")

# btn2 = Button(window, padx=10, pady=5, text="button")
# btn2.pack(side="right")

# btn3 = Button(window, bg="yellow", text="button")
# btn3.pack(side="left")

# Frame Section
frame = Frame(window, relief='solid', bd=1)
frame.pack(fill='x', side = "top")

#Scrollbar Section
scr = Scrollbar(frame)
scr.pack(side="right", fill="y")

# Text Section
txt_box = Text(frame, width=30, height=10, yscrollcommand=scr.set)       #width: numbers of letters // height : numbers of lines
txt_box.pack(fill="both")
scr.config(command=txt_box.yview)

# Label Section
# label = Label(window, text="Hello")
# label.pack(side="top")

dontknow = "Hi"

label_var = Label(window, text=dontknow)
label_var.pack(side="top")

# Entry Section
e = Entry(window, width=30)
e.pack()
e.insert(0, "Plz write only a line")

# Checkbox Section
ch1 = IntVar()
checkbox1 = Checkbutton(window, text="Adult", variable=ch1)
checkbox1.pack()

ch2 = IntVar()
checkbox2 = Checkbutton(window, text="Student", variable=ch2)
checkbox2.pack()

# RadioButton Section
rdbt_frame=Frame(window, relief='solid', bd=1)
rdbt_frame.pack(fill="x")
age = IntVar()
age1 = Radiobutton(rdbt_frame, text="Adult", value=1, variable=age)
age2 = Radiobutton(rdbt_frame, text="Student", value=2, variable=age)
age3 = Radiobutton(rdbt_frame, text="Elder", value=3, variable=age)
age4 = Radiobutton(rdbt_frame, text="Child", value=4, variable=age)

age1.pack(side="left")
age2.pack(side="left")
age3.pack(side="left")
age4.pack(side="left")

def select_age():
    selected_age = age.get()
    if selected_age == 1:
        print("adult")
    elif selected_age == 2:
        print("student")
    elif selected_age == 3:
        print("elder")
    elif selected_age == 4:
        print("child")
        


radio_btn = Button(rdbt_frame, text="Choice", command=select_age)
radio_btn.pack(side="right")

# Combobox Section

btn_frame=Frame(window, relief='solid', bd=1)
btn_frame.pack(fill="x")

cmb_age = ['adult', 'student', 'elder', 'child']
cmbbox = ttk.Combobox(btn_frame, height=4, values=cmb_age, state="readonly")
cmbbox.pack(side="left")

def select_age_cmb():
    selected_age = cmbbox.get()
    print(selected_age)
    # if selected_age == 1:
    #     print("adult")
    # elif selected_age == 2:
    #     print("student")
    # elif selected_age == 3:
    #     print("elder")
    # elif selected_age == 4:
    #     print("child")

cmb_btn = Button(btn_frame, text="Choice", command=select_age_cmb)
cmb_btn.pack(side="right")

# List Section
list_box = Listbox(window, selectmode="extended",height=15, yscrollcommand=scr.set)       #width: numbers of letters // height : numbers of lines
list_box.pack(side="left", fill="both", expand = True)
scr.config(command=list_box.yview)

window.mainloop()