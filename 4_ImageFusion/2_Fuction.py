from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import os
from PIL import Image


window = Tk()
window.title("ROY IMAGE FUSION")

##########Function##########
file_path = f"{os.path.dirname(__file__)}/images"

def add_file():
    files = filedialog.askopenfilenames(title="Select Images", 
                                           filetypes=(('JPG File', '*.jpg'), ("All Files", "*.*")),
                                           initialdir=f"{file_path}")
    for file in files:
        list_box.insert(END, file)

def del_file():
    for index in reversed(list_box.curselection()):
        list_box.delete(index)

def browse_dest_path():
    folder_selected = filedialog.askdirectory(initialdir=f"{file_path}")
    if folder_selected == "":
        return
    dest_path.delete(0,END)
    dest_path.insert(0, folder_selected)
def fusion_image():
    # 1. Width
    img_width = cmb_width.get()
    if img_width == "Original":
        img_width = -1
    else:
        img_width = int(img_width)

    # 2. Format
    img_format = cmb_ext.get().lower()

    # 3. Spacing
    img_space = cmb_space.get()
    if img_space == "Slim":
        img_space = 30
    elif img_space == "Normal":
        img_space = 60
    elif img_space == "Wide":
        img_space = 90
    else : 
        img_space = 0

    # Option Apple
    images = [Image.open(x) for x in list_box.get(0, END)]

    image_size = []
    if img_width > -1 :
        image_size = [(int(img_width), int(img_width * x.size[1] / x.size[0]))for x in images]
    else :
        image_size = [(x.size[0], x.size[1]) for x in images]

    widths, heights = zip(*(image_size))

    max_width, total_height = max(widths), sum(heights)

    if img_space > 0:
        total_height += (img_space * (len(images))-1)

    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0

    for idx, img in enumerate(images):
        if img_width > -1:
            img = img.resize(image_size[idx])
    
        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_space)

        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()
        
    file_name = "fusioned_image." + img_format
    save_path = os.path.join(dest_path.get(), file_name)
    result_img.save(save_path)
    msgbox.showinfo("Notice", "Done")


def start():
    # Check File List
    if list_box.size() == 0 :
        msgbox.showwarning("Warning!", "Add images")
        return
    
    # Check Save Path
    if len(dest_path.get()) == 0:
        msgbox.showwarning("Warning!", "Select save path")
        return

    # Get Options
    fusion_image()

##########Layout############
#File btn frame
file_frame = Frame(window)
file_frame.pack(fill='x', padx = 5, pady = 5)

btn_add_file = Button(file_frame, text ="Add Files", command=add_file)
btn_add_file.pack(side='left', padx = 5, pady = 5)

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

btn_start = Button(run_frame, padx=5, pady=5,text ="Start", command=start)
btn_start.pack(side='right', padx = 5, pady = 5)

window.mainloop()