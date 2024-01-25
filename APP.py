from tkinter import *
import form

LIST_MODE = ['Square','Rectangle','Circle','Disk']

# MAIN FRAME
m=Tk()
m.title("Shape Generator :D")
w = Frame(m,width=854,height=480)

# FRAME TO DRAW
c = Canvas(w,width=480,height=480,background="#555")
c.grid(row=0,column=0)

menu = Frame(w)
# SELECTE MODE
def ModeSelect(evt):
    build_alt_frame(evt)

Lb = Listbox(menu)
for mode in LIST_MODE:
    Lb.insert(END,mode)
Lb.select_set(0)
Lb.bind('<<ListboxSelect>>',ModeSelect)
Lb.grid()


# ALTERNATIVE FRAMES FOR SIZE
def print_ssinbox() :
    print(spinvar_1.get())
    print(spinvar_2.get())

alt_frame = Frame(menu)
spinvar_1 = IntVar()
spinvar_2 = IntVar()
def build_alt_frame(evt):
    for widget in alt_frame.winfo_children():
        widget.destroy()
    alt_label_1 = Label(alt_frame,text="dim_1 :")
    mode = Lb.get(Lb.curselection())
    match(mode):
        case 'Circle' :
            alt_label_1 = Label(alt_frame,text="ray :")
        case 'Disk' :
            alt_label_1 = Label(alt_frame,text="ray :")
        case 'Square':
            alt_label_1 = Label(alt_frame,text="width :")
        case 'Rectangle':
            alt_label_1 = Label(alt_frame,text="width :")
    alt_label_1.grid()
    alt_box_1 = Spinbox(alt_frame, from_=0, to=100, textvariable=spinvar_1,wrap=True)
    alt_box_1.grid()
    if(mode == 'Rectangle'):
        alt_label_2 = Label(alt_frame,text="lenght :")
        alt_label_2.grid()
        alt_box_2 = Spinbox(alt_frame, from_=0, to=100, textvariable=spinvar_2,wrap=True)
        alt_box_2.grid()
    alt_refresh = Button(alt_frame,text="generate",command=print_ssinbox)
    alt_refresh.grid()
    alt_frame.grid()
build_alt_frame(None)
alt_frame.grid()

# END OF WINDOW
menu.grid(row=0,column=1,sticky="N")
w.grid()
m.mainloop()