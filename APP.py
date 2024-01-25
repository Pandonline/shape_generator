from tkinter import *
import form

LIST_MODE = ['Square','Rectangle','Circle','Disk']
MODE = LIST_MODE[0]

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
    MODE = Lb.get(Lb.curselection())
    HideAllSizeFrame(evt)
    match(MODE):
        case 'Circle' :
            circle_frame.grid()
        case 'Disk' :
            circle_frame.grid()
        case 'Square':
            square_frame.grid()
        case 'Rectangle':
            rectangle_frame.grid()
        

Lb = Listbox(menu)
for mode in LIST_MODE:
    Lb.insert(END,mode)
Lb.select_set(0)
Lb.bind('<<ListboxSelect>>',ModeSelect)
Lb.grid()
    
def HideAllSizeFrame(evt):
    circle_frame.grid_forget()
    square_frame.grid_forget()
    rectangle_frame.grid_forget()

# ALTERNATIVE FRAMES FOR SIZE
form_dimension_1 = IntVar()
form_dimension_2 = IntVar()
def print_val_size():
    print(form_dimension_1.get())
    print(form_dimension_2.get())
    print()
    
# Validating function
def validate(user_input):
    # check if the input is numeric
    if  user_input.isdigit():
        # Fetching minimum and maximum value of the spinbox
        minval = 0
        maxval = 150
 
        # check if the number is within the range
        if int(user_input) not in range(minval, maxval):
            print ("Out of range")
            return False
 
        # Printing the user input to the console
        print(user_input)
        return True
 
    # if input is blank string
    elif user_input is "":
        print(user_input)
        return True
 
    # return false is input is not numeric
    else:
        print("Not numeric")
        return False

### CIRCLE FRAME
circle_frame = Frame(menu)
circle_label = Label(circle_frame,text="ray :")
circle_label.grid()
circle_ray = Spinbox(circle_frame, from_=0, to=100,textvariable=form_dimension_1)
circle_ray.grid()
circle_ray.configure(command=print_val_size)

### SQUARE FRAME
square_frame = Frame(menu)
square_label = Label(square_frame,text="width :")
square_label.grid()
square_width = Spinbox(square_frame, from_=0, to=100,textvariable=form_dimension_1)
square_width.grid()
square_width.configure(command=print_val_size)

### RECTANGLE FRAME
rectangle_frame = Frame(menu)
rectangle_label = Label(rectangle_frame,text="width :")
rectangle_label.grid()
rectangle_width = Spinbox(rectangle_frame, from_=0, to=100,textvariable=form_dimension_1)
rectangle_width.grid()
rectangle_width.configure(command=print_val_size)
rectangle_label_2 = Label(rectangle_frame,text="lenght :")
rectangle_label_2.grid()
rectangle_lenght = Spinbox(rectangle_frame, from_=0, to=100,textvariable=form_dimension_2)
rectangle_lenght.grid()
rectangle_lenght.configure(command=print_val_size)


#DEFAULT ALTERNATIVE FRAME
square_frame.grid()

# END OF WINDOW
menu.grid(row=0,column=1,sticky="N")
w.grid()
m.mainloop()