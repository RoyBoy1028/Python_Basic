from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title('Ticket')
window.geometry('640x480')
window.resizable(False, False)

title = '''
        [Roy's Amusement Park]
'''
label_var = Label(window, text=title)
label_var.pack(side="top")

total = {'Adult': 0 , 'Student' : 0, 'Elder' : 0, 'Child' : 0}

result = f'''
Price:
{total}
'''

txt_box = Label(window, text=result ,width= 50, height = 24)
txt_box.pack(side= "bottom")

rdbt_frame=Frame(window, relief='solid', bd=1)
rdbt_frame.pack(fill="x")
age = IntVar()
age1 = Radiobutton(rdbt_frame, text="Adult", value=1, variable=age)
age2 = Radiobutton(rdbt_frame, text="Student", value=2, variable=age)
age3 = Radiobutton(rdbt_frame, text="child", value=3, variable=age)
age4 = Radiobutton(rdbt_frame, text="elder", value=4, variable=age)

def convert_t2label():
    change = txt_box.get("1.0", END)
    label_var.config(text=change)
    txt_box.delete("1.0", END)

age1.pack(side="left")
age2.pack(side="left")
age3.pack(side="left")
age4.pack(side="left")

def select_age():
    selected_age = age.get()
    if selected_age == 1:       #add Adult
        total['Adult'] += 1
    elif selected_age == 2:
        total['Student'] += 1
    elif selected_age == 3:
        total['Child'] += 1
    elif selected_age == 4:
        total['Elder'] += 1

    total_pay = 15 * total['Adult'] + 0 * total['Elder'] + 12 * total ['Student'] + 5 * total['Child']
    
    result = f'''
            Price: $ {total_pay}
            {total}
            '''
    txt_box.config(text = result)

radio_btn = Button(rdbt_frame, text="Add", padx=10, pady=5,command=select_age)
radio_btn.pack(side="right")

window.mainloop()