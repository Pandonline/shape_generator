from tkinter import *
import form

LIST_MODE = ['Square','Rectangle','Circle','Disk']
# MAIN FRAME
m=Tk()
m.title("Shape Generator :D")
w = Frame(m,width=854,height=480)
# MODE LABEL
MODE = Label(m,text=LIST_MODE[0])
# FRAME TO DRAW
c = Canvas(w,width=480,height=480,background="#555")
c.grid(row=0,column=0)

menu = Frame(w)
# SELECTE MODE
def ModeSelect(evt):
    mode = Lb.curselection()
    if len(mode)>0:
        MODE.config(text=Lb.get(mode[0]))
    build_alt_frame(evt)

Lb = Listbox(menu)
for mode in LIST_MODE:
    Lb.insert(END,mode)
Lb.select_set(0)
Lb.bind('<<ListboxSelect>>',ModeSelect)
Lb.grid()


# ALTERNATIVE FRAMES FOR SIZE
def Generate() :
    clearCanvas()
    drawGrid(spinvar_1.get())

alt_frame = Frame(menu)
spinvar_1 = IntVar()
spinvar_2 = IntVar()
def build_alt_frame(evt):
    for widget in alt_frame.winfo_children():
        widget.destroy()
    alt_label_1 = Label(alt_frame,text="dim_1 :")    
    match(MODE.cget("text")):
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
    if(MODE.cget("text") == 'Rectangle'):
        alt_label_2 = Label(alt_frame,text="lenght :")
        alt_label_2.grid()
        alt_box_2 = Spinbox(alt_frame, from_=0, to=100, textvariable=spinvar_2,wrap=True)
        alt_box_2.grid()
    alt_refresh = Button(alt_frame,text="generate",command=Generate)
    alt_refresh.grid()
    alt_frame.grid()
build_alt_frame(None)
alt_frame.grid()

#CANVAS
def clearCanvas():
    c.delete("all")

def drawGrid(nbCase):
    maxX = int(c.cget("width"))
    maxY = int(c.cget("height"))
    for i in range(nbCase):
        c.create_line(i*maxX//nbCase,0,i*maxX//nbCase,maxY)
        c.create_line(0,i*maxY//nbCase,maxX,i*maxY//nbCase)
# END OF WINDOW
menu.grid(row=0,column=1,sticky="N")
w.grid()
m.mainloop()