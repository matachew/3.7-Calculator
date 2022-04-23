from tkinter import *



main = Tk()
main.title("Calculator")
main.configure(bg="#24292e")

main.resizable(False, False)

current = Entry(main, width=35, borderwidth=5)
current.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def on_clear():
    current.delete(0, END)

def on_click(number):
    update = current.get()
    current.delete(0, END)
    current.insert(0, str(update) + str(number) )

def on_equal():
    int2 = current.get()
    current.delete(0, END)

    if operation == "addition":
        current.insert(0, num1 + float(int2))
    if operation == "subtraction":
        current.insert(0, num1 - float(int2))
    if operation == "multiplication":
        current.insert(0, num1 * float(int2))
    if operation == "division":
        current.insert(0, num1 / float(int2))




def on_add():
    int1 = current.get()
    global num1
    global operation 
    operation = "addition"
    num1 = float(int1)
    current.delete(0, END)


def on_minus():
    int1 = current.get()
    global num1
    global operation 
    operation = "subtraction"
    num1 = float(int1)
    current.delete(0, END)

def on_multiply():
    int1 = current.get()
    global num1
    global operation 
    operation = "multiplication"
    num1 = float(int1)
    current.delete(0, END)


def on_divide():
    int1 = current.get()
    global num1
    global operation 
    operation = "division"
    num1 = float(int1)
    current.delete(0, END)






# create objects for each image for hte buttons

img0 = PhotoImage(file="3.7-Calculator/0.png")
img1 = PhotoImage(file="3.7-Calculator/1.png")
img2 = PhotoImage(file="3.7-Calculator/2.png")
img3 = PhotoImage(file="3.7-Calculator/3.png")
img4 = PhotoImage(file="3.7-Calculator/4.png")
img5 = PhotoImage(file="3.7-Calculator/5.png")
img6 = PhotoImage(file="3.7-Calculator/6.png")
img7 = PhotoImage(file="3.7-Calculator/7.png")
img8 = PhotoImage(file="3.7-Calculator/8.png")
img9 = PhotoImage(file="3.7-Calculator/9.png")

imgmultiply = PhotoImage(file="3.7-Calculator/multiply.png")
imgplus = PhotoImage(file="3.7-Calculator/plus.png")
imgminus = PhotoImage(file="3.7-Calculator/minus.png")
imgdivide = PhotoImage(file="3.7-Calculator/divide.png")


button0 = Button(main, text="0", padx=65, pady=20, image=img0, command=lambda: on_click(0)) #footnote 1 at bottom about Lambda
button1 = Button(main, text="1", padx=20, pady=20, command=lambda: on_click(1))
button2 = Button(main, text="2", padx=20, pady=20, command=lambda: on_click(2))
button3 = Button(main, text="3", padx=20, pady=20, command=lambda: on_click(3))
button4 = Button(main, text="4", padx=20, pady=20, command=lambda: on_click(4))
button5 = Button(main, text="5", padx=20, pady=20, command=lambda: on_click(5))
button6 = Button(main, text="6", padx=20, pady=20, command=lambda: on_click(6))
button7 = Button(main, text="7", padx=20, pady=20, command=lambda: on_click(7))
button8 = Button(main, text="8", padx=20, pady=20, command=lambda: on_click(8))
button9 = Button(main, text="9", padx=20, pady=20, command=lambda: on_click(9))

equalbutton = Button(main, text="=", padx=20, pady=20, command=on_equal)
clearbutton = Button(main, text="C", padx=20, pady=20, command=on_clear)
plusbutton = Button(main, text="+", padx=20, pady=20, command=on_add)
minusbutton = Button(main, text="-", padx=20, pady=20, command=on_minus)
multiplybutton = Button(main, text="x", padx=20, pady=20, command=on_multiply)
dividebutton = Button(main, text="/", padx=20, pady=20, command=on_divide)

decimalbutton = Button(main, text=".", padx=20, pady=20, command=lambda: on_click("."))

                                                          
# making button widgets or objects or something for the GUI

button0.grid(row=5, column=0, columnspan = 2)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

clearbutton.grid(row=1, column=0)
dividebutton.grid(row=1, column=3)
multiplybutton.grid(row=2, column=3)
minusbutton.grid(row=3, column=3)
plusbutton.grid(row=4, column=3)
equalbutton.grid(row=5, column=3)
decimalbutton.grid(row=5, column=2)

main.mainloop()

#Fn1 (l17) since we cant put function parameters through buttons we have to use lambda