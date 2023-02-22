from tkinter import *
from tkinter import messagebox

from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    password_entry.delete(0, END)
    password_list = []

    for char in range(1, randint(8, 10) + 1):
        password_list.append(choice(letters))

    for char in range(1, randint(2, 4) + 1):
        password_list += choice(symbols)

    for char in range(1, randint(2, 4) + 1):
        password_list += choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(user_entry.get()) == 0 or len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        if messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail/Username: {user_entry.get()} " f"\nPassword: {password_entry.get()} \nIs it ok to save?"):
            with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day29-password-manager-project\data.txt", mode="a") as data: 
                data.write(f'{website_entry.get().title()} | {user_entry.get()} | {password_entry.get()}\n')
                data.close()
            pyperclip.copy(password_entry.get())
            messagebox.showinfo(title="Success!", message="The password was copied to the clipboard.")
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file=r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day29-password-manager-project\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0,column=1)

website_lb = Label(text="Website:", bg="white")
website_lb.grid(row=1, column=0)
website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

user_lb = Label(text="Email/Username:", bg="white")
user_lb.grid(row=2, column=0)
user_entry = Entry(width=42)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "mikybrambilla@gmail.com")

password_lb = Label(text="Password:", bg="white")
password_lb.grid(row=3, column=0)
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)
gen_pass_button = Button(text="Generate Password", command=gen_password)
gen_pass_button.grid(row=3, column=2)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()