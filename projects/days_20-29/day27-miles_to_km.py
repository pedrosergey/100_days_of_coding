# import the necessary library

from tkinter import *

# create and configure the screen

tk = Tk()
tk.title("Kilometers to Mile converter")
tk.minsize(width=200, height=200)
tk.config(padx=25, pady=25)


# create a function that reads the content of the input

def km_converter():
    km = float(entry.get())
    miles = round(km * 0.621371, 2)
    label_4["text"] = str(miles)

# create and configure the rest of the objects

label_1 = Label()
label_1.grid(column=0, row=0)

label_2 = Label(text="Kms")
label_2.grid(column=2, row=0)

label_3 = Label(text="is equal to")
label_3.grid(column=0, row=1)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)

label_5 = Label(text="Miles")
label_5.grid(column=2, row=1)

button = Button(text= "Convert!", command= km_converter, pady= 5, padx= 5)
button.grid(column=1, row=2)

entry = Entry(width=10)
entry.grid(column=1, row=0)

tk.mainloop()
