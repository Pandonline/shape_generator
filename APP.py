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

Lb = Listbox(m)
for mode in LIST_MODE:
    Lb.insert(END,mode)
Lb.bind('<<ListboxSelect>>',ModeSelect)
Lb.grid(row=0,column=1)

# END OF WINDOW
w.grid()
m.mainloop()