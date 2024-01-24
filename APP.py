from tkinter import *
import form

LIST_MODE = ['Square','Rectangle','Circle','Disk']
MODE = LIST_MODE[0]

# MAIN FRAME
m=Tk()
m.title("Shape Generator :D")
w = Frame(m,width=854,height=480)

# FRAME TO DRAW
c = Canvas(w,width=480,height=480)
c.grid()

# SELECTE MODE
def ModeSelect(evt):
    MODE = Lb.get(Lb.curselection())
    if(MODE in ['Circle','Disk']):
        circle_frame.grid(row=1,column=1)
        square_frame.grid_forget()
    else :
        circle_frame.grid_forget()
        square_frame.grid(row=1,column=1)

Lb = Listbox(m)
for mode in LIST_MODE:
    Lb.insert(END,mode)
Lb.bind('<<ListboxSelect>>',ModeSelect)
Lb.grid(row=0,column=1)
    
### CIRCLE FRAME
circle_frame = Frame(m)
circle_label = Label(circle_frame,text="ray")
circle_label.grid()

### SQUARE FRAME
square_frame = Frame(m)
square_label = Label(square_frame,text="width")
square_label.grid()

# END OF WINDOW
w.grid()
m.mainloop()