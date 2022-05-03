from tkinter import *
from PIL import Image, ImageTk

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

img0 = Image.open("3.7-Calculator/0.png")
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
imgequal = PhotoImage(file="3.7-Calculator/equal.png")

szdimg0 = img0.resize((300, 300), Image.ANTIALIAS)
rzd_img0= ImageTk.PhotoImage(szdimg0)

szdimg1 = img1.resize((100, 100), Image.ANTIALIAS)
rzd_img1= ImageTk.PhotoImage(szdimg1)


button0 = Button(main, text="0", image=rzd_img0, command=lambda: on_click(0), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,) #footnote 1 at bottom about Lambda
button1 = Button(main, text="1", image=rzd_img1, command=lambda: on_click(1), borderwidth=0, highlightthickness=0, bd=0, highlightbackground='#24292e')
button2 = Button(main, text="2", image=img2, command=lambda: on_click(2), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button3 = Button(main, text="3", bg="#24292e", image=img3, command=lambda: on_click(3), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button4 = Button(main, text="4", image=img4, command=lambda: on_click(4), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button5 = Button(main, text="5", image=img5, command=lambda: on_click(5), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button6 = Button(main, text="6", image=img6, command=lambda: on_click(6), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button7 = Button(main, text="7", image=img7, command=lambda: on_click(7), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button8 = Button(main, text="8", image=img8, command=lambda: on_click(8), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button9 = Button(main, text="9", image=img9, command=lambda: on_click(9), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)

equalbutton = Button(main, image=imgequal, text="=", borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_equal)
clearbutton = Button(main, text="C",  borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_clear)
plusbutton = Button(main, text="+", image=imgplus, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_add)
minusbutton = Button(main, text="-", image=imgminus, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_minus)
multiplybutton = Button(main, text="x", borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, image=imgmultiply, command=on_multiply)
dividebutton = Button(main, text="/", borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, image=imgdivide, command=on_divide)

decimalbutton = Button(main, text=".", borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=lambda: on_click("."))

                                                          
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