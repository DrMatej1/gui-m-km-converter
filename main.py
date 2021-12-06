from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=200, height=150)

input = Entry(width=10)
input.grid(column = 1, row = 0)


my_label = Label(text="is equal to")
my_label.grid(column = 0, row = 1)

my1_label = Label(text="Miles")
my1_label.grid(column = 2, row = 0)

my2_label = Label(text="km")
my2_label.grid(column = 2, row = 1)

def button_click():
    my3_label["text"] = int(input.get()) * 1.6


button = Button(text="Button", command=button_click)
button.grid(column = 1, row = 2)

my3_label = Label(text="0")
my3_label.grid(column = 1, row = 1)




window.mainloop()
