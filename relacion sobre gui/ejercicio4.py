"""Construye un interfaz que represente una calculadora con cifras 0,...,9 y los operadores
+,-,*,/"""


from Tkinter import* 

calculator = Tk() 
calculator.title('Calculator') 
calculator.geometry('197x150') 

menubar = Menu(calculator) 

#----------Toplevel 
def toplevel(): 
    toplevel = Toplevel(calculator) 

#----------view menu 
def standard(): 
    toplevel() 
viewMenu = Menu(menubar, tearoff = 0)     
viewMenu.add_command(label="Standard                Alt+1",
command=standard) 
menubar.add_cascade(label="View", menu=viewMenu) 
#----------edit 
def editMenu(): 
    toplevel() 
editMenu = Menu(menubar, tearoff = 0) 
editMenu.add_command(label="Copy                    Ctrl+C",
command=editMenu) 
menubar.add_cascade(label="Edit", menu=editMenu) 
#----------help 
def viewHelp(): 
    toplevel() 
helpMenu = Menu(menubar, tearoff = 0) 
helpMenu.add_command(label="View Help                   F1",
command=viewHelp) 
menubar.add_cascade(label="Help", menu=helpMenu) 

screen = Frame(calculator, bd=0, width=150, height=25, relief=SUNKEN)
buttons = Frame(calculator, bd=0, width=5, height=1, relief=GROOVE)
screen.grid(column=0, row=0, padx=0, pady=0) 
buttons.grid(column=0, row=1, padx=1) 

def appear(x): 
    return lambda: results.insert(END, x) 

def Zero(): 
    results.insert(END, "0") 
    return 

def Equals(): 
    try: 
        result = eval(results.get()) 
    except: 
        result = "Invalid sum" 
    results.delete(0, END) 
    results.insert(0, result) 
     
numbers=["7", "4", "1","8", "5", "2","9", "6", "3"] 

for index in range(9): 
    n=numbers[index] 
    Button(buttons, bg="White", text=n, width=5, height=1,
command=appear(n), relief=GROOVE).grid(padx=2, pady=2, row=index%3,
column=index/3)  

zero= Button(buttons, bg="White", text="0", width=5, height=1,
command=Zero, relief=GROOVE) 
zero.grid(padx=2, pady=2, column=1, row=3) 



functions=["/", "*", "-", "+"] 
for index in range(4): 
    f=functions[index] 
    Button(buttons, bg="White", text=f, width=5, height=1,command=appear(f), relief=GROOVE).grid(padx=2, pady=2, row=index%4,column=3)  

equals= Button(buttons, bg="White", text="=", width=5, height=1,
command=Equals, relief=GROOVE) 
equals.grid(ipadx=2, pady=2, row=3, column=2) 

numbers = StringVar() 
results = Entry(screen, textvariable=numbers, width=19, fg="#003366",
bg="#f2f2f2", font="Verdana") 
results.pack() 

calculator.config(menu=menubar) 
calculator.mainloop()
