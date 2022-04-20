from tkinter import *



main = Tk()
main.title("Calculator")

main.resizable(False, False)

current = Entry(main, width=35, borderwidth=5)
current.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#e.insert(0, "")
def on_click(number):
    update = current.get()
    current.delete(0, END)
    current.insert(0, str(update) + str(number) )

button0 = Button(main, text="0", padx=100, pady=20, command=lambda: on_click(0)) #footnote 1 at bottom about Lambda
button1 = Button(main, text="1", padx=40, pady=20, command=lambda: on_click(1))
button2 = Button(main, text="2", padx=40, pady=20, command=lambda: on_click(2))
button3 = Button(main, text="3", padx=40, pady=20, command=lambda: on_click(3))
button4 = Button(main, text="4", padx=40, pady=20, command=lambda: on_click(4))
button5 = Button(main, text="5", padx=40, pady=20, command=lambda: on_click(5))
button6 = Button(main, text="6", padx=40, pady=20, command=lambda: on_click(6))
button7 = Button(main, text="7", padx=40, pady=20, command=lambda: on_click(7))
button8 = Button(main, text="8", padx=40, pady=20, command=lambda: on_click(8))
button9 = Button(main, text="9", padx=40, pady=20, command=lambda: on_click(9))

equalbutton = Button(main, text="=", padx=20, pady=20, command=lambda: on_click())
clearbutton = Button(main, text="C", padx=20, pady=20, command=lambda: on_click())
plusbutton = Button(main, text="+", padx=40, pady=20, command=lambda: on_click())
minusbutton = Button(main, text="-", padx=20, pady=20, command=lambda: on_click())
multiplybutton = Button(main, text="x", padx=20, pady=20, command=lambda: on_click())
dividebutton = Button(main, text="/", padx=20, pady=20, command=lambda: on_click())

                                                          
# making button widgets or objects or something for the GUI

button0.grid(row=4, column=0, columnspan = 2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

clearbutton.grid(row=1, column=3)
dividebutton.grid(row=2, column=3)
multiplybutton.grid(row=3, column=3)
minusbutton.grid(row=4, column=3)
plusbutton.grid(row=4, column=2)

main.mainloop()

#Fn1 (l17) since we cant put function parameters through buttons we have to use lambda