from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Yossi Calculator")
root.iconbitmap('c:/Users/yossi/OneDrive/Documents/python projects/calcicon.ico')


"""
frame = Tk.frame(root, bg="White")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
"""
"""
def myClick():
    myLabel = Label(root, text = "Welcome to guess my number game!, Lets  S T A R T! ")
    myLabel.pack()

myLabel1 = Label(root, text="Hello")
myLabel2 = Label(root, text="Welcome to tic tac toe game!")

myLabel1.pack()
myLabel2.pack()


myButton = Button(root, text="Start game!", padx=100, pady=30, bg="#264D42", command = myClick)
myButton.pack()
"""
"""
frame = Frame(root, bg="brown")
frame.place(relwidth=0.9, relheight=0.9, relx=0.2, rely=0.2)
"""

e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_clear():
    e.delete(0, END)


def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "substraction":
        e.insert(0, int(f_num) - int(second_number))
    
    elif math == "multiplication":
        e.insert(0, int(second_number) * int(f_num))

    elif math == "division":
        e.insert(0, int(f_num) / int(second_number))

    elif math == "addition":
        e.insert(0, int(second_number) + int(f_num))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

button_1 = Button(root,text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root,text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root,text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root,text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root,text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root,text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root,text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root,text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root,text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root,text="0", padx=40, pady=20, command=lambda: button_click(0))
button_quit = Button(root, text="Quit Calculator", padx= 60, pady=10, bg="#009888", command=root.quit)


button_add = Button(root,text="+", padx=39, pady=20, command=button_add) 
button_equal = Button(root,text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root,text="clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=43, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=43, pady=20, command=button_divide)




button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_quit.grid(row=7,column=0, columnspan=3)

root.mainloop()

