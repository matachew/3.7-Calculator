from tkinter import *

root = Tk()

e = Entry(root)
e.grid(row=3, column=3)
e.get


def myClick():
    myLabel3 = Label(root, text="Look i pressed a button")

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is is is is ")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)


myButton = Button(root, text="Click me",  padx=50, pady=50, command=myClick)


myButton.grid(row=2, column=2)


root.mainloop()