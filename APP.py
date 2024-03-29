from tkinter import *
from tkinter import colorchooser
import form
import random
import Randomizer


def clone_widget(widget, master=None):
    """
    Create a cloned version o a widget

    Parameters
    ----------
    widget : tkinter widget
        tkinter widget that shall be cloned.
    master : tkinter widget, optional
        Master widget onto which cloned widget shall be placed. If None, same master of input widget will be used. The
        default is None.

    Returns
    -------
    cloned : tkinter widget
        Clone of input widget onto master widget.

    """
    # Get main info
    parent = master if master else widget.master
    cls = widget.__class__

    # Clone the widget configuration
    cfg = {key: widget.cget(key) for key in widget.configure()}
    cloned = cls(parent, **cfg)

    # Clone the widget's children
    for child in widget.winfo_children():
        child_cloned = clone_widget(child, master=cloned)
        if child.grid_info():
            grid_info = {k: v for k, v in child.grid_info().items() if k not in {'in'}}
            child_cloned.grid(**grid_info)
        elif child.place_info():
            place_info = {k: v for k, v in child.place_info().items() if k not in {'in'}}
            child_cloned.place(**place_info)
        else:
            pack_info = {k: v for k, v in child.pack_info().items() if k not in {'in'}}
            child_cloned.pack(**pack_info)

    return cloned

LIST_MODE = ['Square','Rectangle','Circle','Disk','Ring']
# MAIN FRAME
m=Tk()
m.title("Shape Generator :D")
w = Frame(m,width=854,height=480)
# MODE LABEL
MODE = Label(m,text=LIST_MODE[0])
# FRAME TO DRAW
c = Canvas(w,width=480,height=480,background="#DDD")
c.grid(row=0,column=0)

menu = Frame(w)
# SELECTE MODE
def ModeSelect(evt):
    mode = Lb.curselection()
    if len(mode)>0:
        MODE.config(text=Lb.get(mode[0]))
    build_alt_frame(evt)
    Generate()

Lb = Listbox(menu)
for mode in LIST_MODE:
    Lb.insert(END,mode)
Lb.select_set(0)
Lb.bind('<<ListboxSelect>>',ModeSelect)
Lb.grid()

# ALTERNATIVE FRAMES FOR SIZE
    
alt_frame = Frame(menu)
spinvar_1 = IntVar()
spinvar_2 = IntVar()
def build_alt_frame(evt):
    for widget in alt_frame.winfo_children():
        widget.destroy()
    alt_label_1 = Label(alt_frame,text="dim_1 :")
    alt_box_1 = Spinbox(alt_frame, from_=1, to=100, textvariable=spinvar_1,wrap=True)  
    alt_label_2 = Label(alt_frame,text="dim_2 :")
    alt_box_2 = Spinbox(alt_frame, from_=1, to=100, textvariable=spinvar_2,wrap=True)
    match(MODE.cget("text")):
        case 'Circle' :
            alt_label_1.config(text=" Circle Ray :")
            alt_label_1.grid()
            alt_box_1.grid()
        case 'Disk' :
            alt_label_1.config(text="Disk Ray : ")
            alt_label_1.grid()
            alt_box_1.grid()
        case 'Square':
            alt_label_1.config(text="Square Side Size : ")
            alt_label_1.grid()
            alt_box_1.grid()
        case 'Rectangle':
            alt_label_1.config(text="Rectangle Width :")
            alt_label_1.grid()
            alt_box_1.grid()
            alt_label_2.config(text="Rectangle length :")
            alt_label_2.grid()
            alt_box_2.grid()
        case 'Ring':
            alt_label_1.config(text="Outer Ray :")
            alt_label_1.grid()
            alt_box_1.grid()
            alt_label_2.config(text="Inner Ray :")
            alt_label_2.grid()
            alt_box_2.grid()
    alt_refresh = Button(alt_frame,text="generate",command=Generate)
    alt_refresh.grid()
    alt_frame.grid()


#COLOR PICKER
cframe = Frame(menu,pady=15)
ctext = Label(cframe, text="Color Section : ")
ctext.grid()
csize = IntVar(cframe,value=0)
def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    return color_code
def add_color_line():
    csize.set(min(5,csize.get()+1))
    LIST_COLOR_PICKER[csize.get()-1].grid(sticky="W")
    get_list_valeur_color_scroll()
def dec_color_line():
    if(csize.get()>1):
        LIST_COLOR_PICKER[csize.get()-1].grid_forget()
    csize.set(max(1,csize.get()-1))
    get_list_valeur_color_scroll()

cAddDecFrame = Frame(cframe,padx=2,pady=2)
add_button = Button(cAddDecFrame, text="+", command=add_color_line)
add_button.grid(row=1,column=0)
dec_button = Button(cAddDecFrame, text="-", command=dec_color_line)
dec_button.grid(row=1,column=1)
cAddDecFrame.grid()
cListFrame = Frame(cframe)

def color_changer(var):
    color = choose_color()
    LIST_COLOR[var].set(color[1])
    refresh_list()
def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))
cligne = Frame(cListFrame,pady=2)
LIST_COLOR = [ StringVar(cframe) for i in range(5) ]
for c_iter in LIST_COLOR : 
    random_color()
    c_iter.set(random_color())
cligne_button = Button(cligne,text="c")
cligne_label = Label(cligne)

# Randomizer
def get_list_valeur_color_scroll(evt=None):
    li = []
    for i in range(csize.get()):
        li.append([LIST_COLOR[i].get(),LIST_COLOR_PICKER[i].winfo_children()[2].get()])
    return li


cslide = Scale(cligne,from_=1,to=99,orient="horizontal",command=get_list_valeur_color_scroll)
cligne_button.grid()
cligne_label.grid(row=0,column=1)
cslide.grid(row=0,column=2)
LIST_COLOR_PICKER = [clone_widget(cligne) for i in range(5)]
def refresh_list() :
    LIST_COLOR_PICKER[0].winfo_children()[0].configure(command=lambda:color_changer(0),background=LIST_COLOR[0].get())
    LIST_COLOR_PICKER[0].winfo_children()[1].configure(text=LIST_COLOR[0].get())
    LIST_COLOR_PICKER[1].winfo_children()[0].configure(command=lambda:color_changer(1),background=LIST_COLOR[1].get())
    LIST_COLOR_PICKER[1].winfo_children()[1].configure(text=LIST_COLOR[1].get())
    LIST_COLOR_PICKER[2].winfo_children()[0].configure(command=lambda:color_changer(2),background=LIST_COLOR[2].get())
    LIST_COLOR_PICKER[2].winfo_children()[1].configure(text=LIST_COLOR[2].get())
    LIST_COLOR_PICKER[3].winfo_children()[0].configure(command=lambda:color_changer(3),background=LIST_COLOR[3].get())
    LIST_COLOR_PICKER[3].winfo_children()[1].configure(text=LIST_COLOR[3].get())
    LIST_COLOR_PICKER[4].winfo_children()[0].configure(command=lambda:color_changer(4),background=LIST_COLOR[4].get())
    LIST_COLOR_PICKER[4].winfo_children()[1].configure(text=LIST_COLOR[4].get())
    get_list_valeur_color_scroll()
add_color_line()
refresh_list()
cListFrame.grid(sticky="W")

# CANVAS

def clearCanvas():
    c.delete("all")

def drawForm(TAB):
    s = (int(c.cget("width"))-10)/max(len(TAB),len(TAB[0]))
    for i in range(len(TAB)):
        for j in range(len(TAB[0])):
            match(TAB[i][j]):
                case '.' :
                    c.create_rectangle(5+i*s,5+j*s,5+(i+1)*s,5+(j+1)*s)
                case _ : 
                    c.create_rectangle(5+i*s,5+j*s,5+(i+1)*s,5+(j+1)*s,fill=TAB[i][j])

def Generate() :
    clearCanvas()
    TAB = [[]]
    match(MODE.cget("text")):
        case 'Circle' :
            TAB = form.circle(spinvar_1.get())
        case 'Disk' :
            TAB = form.disk(spinvar_1.get())
        case 'Square':
            TAB = form.square(spinvar_1.get())
        case 'Rectangle':
            TAB = form.rect(spinvar_1.get(),spinvar_2.get())
        case 'Ring':
            TAB = form.ring(spinvar_1.get(),spinvar_2.get())
    TAB = Randomizer.rand_form(TAB,get_list_valeur_color_scroll())
    # form.pp(TAB)
    drawForm(TAB)
    generateCountFrame(TAB)
    
# COUNT BLOCK

countFrame = Frame(m)


countSubLigneFrame = Frame(countFrame)
countSubCanva = Canvas(countSubLigneFrame,width=10,height=10)
countSubCanva.grid(row=0,column=0)
countSubLabel = Label(countSubLigneFrame,text="color number : nb iter")
countSubLabel.grid(row=0,column=1)


def forgetCount(size):
    for i in range(size):
        LIST_COUNT_OBJ.pop().grid_forget()
def revealCount():
    for i in LIST_COUNT_OBJ:
        i.grid(sticky='W')
        
def generateCountFrame(TAB):
    countDico = {}
    for i in range(len(TAB)):
        for j in range(len(TAB[0])):
            if TAB[i][j] in countDico:
                countDico[TAB[i][j]] = countDico.get(TAB[i][j]) + 1
            else :
                countDico[TAB[i][j]] = 1
    if('.' in countDico.keys()):
        countDico.pop('.')
    forgetCount(len(LIST_COUNT_OBJ))
    for i in range(len(countDico.keys())):
        LIST_COUNT_OBJ.append(clone_widget(countSubLigneFrame))
    i=0
    for item in sorted(countDico.items(), key=lambda x:x[1],reverse=True):
        LIST_COUNT_OBJ[i].winfo_children()[0].configure(background=item[0])
        LIST_COUNT_OBJ[i].winfo_children()[1].configure(text=item[0]+" : "+str(item[1]))
        i+=1
    revealCount()
LIST_COUNT_OBJ = [clone_widget(countSubLigneFrame)]
# END OF WINDOW
Generate()
build_alt_frame(None)
alt_frame.grid()
menu.grid(row=0,column=1,sticky="N")
cframe.grid()
w.grid()
countFrame.grid(sticky='W')
m.mainloop()