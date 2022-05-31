from tkinter import * # imports tkinter module but all of it
from PIL import Image, ImageTk # imports the pillow module but only the Image and ImageTK names

main = Tk() # creates a tkinter window
main.title("Calculator") # sets the title of the window 
main.configure(bg="#24292e") # sets the bg colour of the window

main.resizable(False, False) # makes the window non-resizzable which i think looks cleaner for the calculator

errorlist = ["Value Error - two decimal places or ", "Name Error - Unknown", "Zero Divison Error - unable to divide by 0"]


current = Entry(main, width=35, borderwidth=5, ) # makes a entry box object as a variable


current.grid(row=0, column=0, columnspan=4, padx=10, pady=10 ) # places the object into the tkinter grid in 0,0

def on_clear(): # makes a function for the clear button 
    current.delete(0, END) # deletes the "current" variable but the first int. on the table

def on_click(number): # makes a function with a variable that gets changed when the function is called 
    update = current.get() # updates the current int. in the variable 
    current.delete(0, END) # then deletes the current variable
    current.insert(0, str(update) + str(number) ) # updates current to be a string and then adds the new string of the updated number

def on_equal(): # makes a function for the equal button 
    int2 = current.get() # makes a second variable that we use for the a operation
    current.delete(0, END) # deletes the current variable
    try:
        if operation == "addition": # if the operation variable = addition then:
            current.insert(0, num1 + float(int2)) # gets the num1 variable and adds it to the int2 variable but also floats it so then we can have decimals
        if operation == "subtraction": # if the operation variable = subtraction then:
            current.insert(0, num1 - float(int2))# gets the num1 variable and subtracts it to the int2 variable
        if operation == "multiplication": # if the operation variable = multiplication then:
            current.insert(0, num1 * float(int2)) # gets the num1 variable and multiplies it to the int2 variable
        if operation == "division": # if the operation variable = division then:
            current.insert(0, num1 / float(int2)) # gets the num1 variable and divides it to the int2 variable
    except (ValueError):
        print("error in calculator")
        current.delete(0, END)
        current.insert(0, str(errorlist[0]) )
    except (ZeroDivisionError):
        print("Zero Divison Error")
        current.delete(0, END)
        current.insert(0, str(errorlist[2]) )




def on_add(): # makes a function for add button
    int1 = current.get()
    global num1 # makes the num1 variable global
    global operation # makes the operation variable global
    operation = "addition" # makes the operation variable = addition 
    try:
        num1 = float(int1) # makes the int1 variable float for 
    except (ValueError):
        print("error in calculator")
        current.delete(0, END)
        current.insert(0, str(errorlist[0]) )
    except (ZeroDivisionError):
        print("Zero Divison Error")
        current.delete(0, END)
        current.insert(0, str(errorlist[2]) )
    current.delete(0, END)


def on_minus():
    int1 = current.get()
    global num1
    global operation 
    operation = "subtraction"
    try:
        num1 = float(int1)
    except (ValueError):
        print("error in calculator")
        current.delete(0, END)
        current.insert(0, str(errorlist[0]) )
    except (ZeroDivisionError):
        print("Zero Divison Error")
        current.delete(0, END)
        current.insert(0, str(errorlist[2]) )

    current.delete(0, END)

def on_multiply():
    int1 = current.get()
    global num1
    global operation 
    operation = "multiplication"
    try:
        num1 = float(int1)
    except (ValueError):
        print("error in calculator")
        current.delete(0, END)
        current.insert(0, str(errorlist[0]) )
    except (ZeroDivisionError):
        print("Zero Divison Error")
        current.delete(0, END)
        current.insert(0, str(errorlist[2]) )



def on_divide():
    int1 = current.get()
    global num1
    global operation 
    operation = "division"
    try:
        num1 = float(int1)
    except (ValueError):
        print("error in calculator")
        current.delete(0, END)
        current.insert(0, str(errorlist[0]) )
    except (ZeroDivisionError):
        print("Zero Divison Error")
        current.delete(0, END)
        current.insert(0, str(errorlist[2]) )
        
    current.delete(0, END)






# get the image files to overlay the buttons

img0 = Image.open("0.png") # opens the image file

img1 = Image.open("1.png") # opens the image file

img2 = Image.open("2.png") # opens the image file

img3 = Image.open("3.png") # opens the image file

img4 = Image.open("4.png") # opens the image file

img5 = Image.open("5.png") # opens the image file

img6 = Image.open("6.png") # opens the image file

img7 = Image.open("7.png") # opens the image file

img8 = Image.open("8.png") # opens the image file

img9 = Image.open("9.png") # opens the image file

imgmultiply = Image.open("multiply.png") # opens the image file
imgplus = Image.open("plus.png") # opens the image file
imgminus = Image.open("minus.png") # opens the image file
imgdivide = Image.open("divide.png") # opens the image file
imgequal = Image.open("equal.png") # opens the image file
imgclear =Image.open("clear.png") # opens the image file
imgdecimal = Image.open("decimal.png") # opens the image file

#resize images
szdimg0 = img0.resize((165, 75), Image.ANTIALIAS)  # resizes the image and stores it as a new variable 
rzd_img0= ImageTk.PhotoImage(szdimg0) # constructs a new image based on last cmd

szdimg1 = img1.resize((75, 75), Image.ANTIALIAS)
rzd_img1= ImageTk.PhotoImage(szdimg1)

szdimg2 = img2.resize((75, 75), Image.ANTIALIAS)
rzd_img2= ImageTk.PhotoImage(szdimg2)

szdimg3 = img3.resize((75, 75), Image.ANTIALIAS)
rzd_img3= ImageTk.PhotoImage(szdimg3)

szdimg4 = img4.resize((75, 75), Image.ANTIALIAS)
rzd_img4= ImageTk.PhotoImage(szdimg4)

szdimg5 = img5.resize((75, 75), Image.ANTIALIAS)
rzd_img5= ImageTk.PhotoImage(szdimg5)

szdimg6 = img6.resize((75, 75), Image.ANTIALIAS)
rzd_img6= ImageTk.PhotoImage(szdimg6)

szdimg7 = img7.resize((75, 75), Image.ANTIALIAS)
rzd_img7= ImageTk.PhotoImage(szdimg7)

szdimg8 = img8.resize((75, 75), Image.ANTIALIAS)
rzd_img8= ImageTk.PhotoImage(szdimg8)

szdimg9 = img9.resize((75, 75), Image.ANTIALIAS)
rzd_img9= ImageTk.PhotoImage(szdimg9)

szdimgequal = imgequal.resize((75, 75), Image.ANTIALIAS)
rzd_imgequal= ImageTk.PhotoImage(szdimgequal)

szdimgdivide = imgdivide.resize((75, 75), Image.ANTIALIAS)
rzd_imgdivide= ImageTk.PhotoImage(szdimgdivide)

szdimgmultiply = imgmultiply.resize((75, 75), Image.ANTIALIAS)
rzd_imgmultiply= ImageTk.PhotoImage(szdimgmultiply)

szdimgminus = imgminus.resize((75, 75), Image.ANTIALIAS)
rzd_imgminus= ImageTk.PhotoImage(szdimgminus)

szdimgplus = imgplus.resize((75, 75), Image.ANTIALIAS)
rzd_imgplus= ImageTk.PhotoImage(szdimgplus)

szdimgclear = imgclear.resize((75, 75), Image.ANTIALIAS)
rzd_imgclear= ImageTk.PhotoImage(szdimgclear)

szdimgdecimal = imgdecimal.resize((75, 75), Image.ANTIALIAS)
rzd_imgdecimal= ImageTk.PhotoImage(szdimgdecimal)

button0 = Button(main, text="0", image=rzd_img0, command=lambda: on_click(0), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,) #footnote 1 at bottom about Lambda
button1 = Button(main, text="1", image=rzd_img1, command=lambda: on_click(1), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button2 = Button(main, text="2", image=rzd_img2, command=lambda: on_click(2), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,) # makes a button, overlays "rzd_img1", runs "onclick" cmd when button pressed, sets borderwidth, highlight, padding to 0 screenunits
button3 = Button(main, text="3", image=rzd_img3, command=lambda: on_click(3), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button4 = Button(main, text="4", image=rzd_img4, command=lambda: on_click(4), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button5 = Button(main, text="5", image=rzd_img5, command=lambda: on_click(5), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button6 = Button(main, text="6", image=rzd_img6, command=lambda: on_click(6), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button7 = Button(main, text="7", image=rzd_img7, command=lambda: on_click(7), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button8 = Button(main, text="8", image=rzd_img8, command=lambda: on_click(8), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)
button9 = Button(main, text="9", image=rzd_img9, command=lambda: on_click(9), borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0,)

equalbutton = Button(main, text="=", image=rzd_imgequal, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_equal)
clearbutton = Button(main, text="C", image=rzd_imgclear, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_clear)
plusbutton = Button(main, text="+", image=rzd_imgplus, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_add)
minusbutton = Button(main, text="-", image=rzd_imgminus, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_minus)
multiplybutton = Button(main, text="x",image=rzd_imgmultiply, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_multiply)
dividebutton = Button(main, text="/", image=rzd_imgdivide, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=on_divide)
decimalbutton = Button(main, text=".", image=rzd_imgdecimal, borderwidth=0, highlightthickness=0, padx=0, pady=0, bd=0, command=lambda: on_click("."))

                                                          
# making button widgets or objects or something for the GUI

button0.grid(row=5, column=0, columnspan = 2) # maps button0 to the tkinter grid on row 5, column 0 and spanning 2 columns 

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

main.mainloop() # runs the main loop 

#Fn1 (l17) since we cant put function parameters through buttons we have to use lambda