from tkinter import *

def calculate():
    r = float(entry.get())*1.60934
    result.config(text= "%.2f" % r)

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=250,height=150)
window.config(padx=20, pady=20)

entry = Entry(width=20)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_eq = Label(text="is equal to")
is_eq.grid(column=0, row=1)

result = Label(text="0")
result.config(justify="center")
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=3)

window.mainloop()