from tkinter import *

main = Tk()
main.title("Calculator")

current = Entry(main, width=35, borderwidth=5)
current.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def add_to():
    return

button0 = Button(main, text="0", padx=40, pady=20, command=add_to)
button1 = Button(main, text="1", padx=40, pady=20, command=add_to)
button2 = Button(main, text="2", padx=40, pady=20, command=add_to)
button3 = Button(main, text="3", padx=40, pady=20, command=add_to)
button4 = Button(main, text="4", padx=40, pady=20, command=add_to)
button5 = Button(main, text="5", padx=40, pady=20, command=add_to)
button6 = Button(main, text="6", padx=40, pady=20, command=add_to)
button7 = Button(main, text="7", padx=40, pady=20, command=add_to)
button8 = Button(main, text="8", padx=40, pady=20, command=add_to)
button9 = Button(main, text="9", padx=40, pady=20, command=add_to)

main.mainloop()