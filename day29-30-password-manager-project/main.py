from tkinter import *
from tkinter import messagebox
import json
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
def save_json_file(new_data):
    try:
        with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day29-30-password-manager-project\data.json", mode="r") as data_file: 
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
    finally:
        with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day29-30-password-manager-project\data.json", mode="w") as data_file: 
            json.dump(data, data_file, indent=4)

def empty_fields(email, password, website):
    return len(email) == 0 or len(password) == 0 or len(website) == 0

def save():
    website = website_entry.get().title()
    password = password_entry.get()
    email = user_entry.get()
    new_data = {website:{"username/email":email, "password":password}} 

    if empty_fields(email, password, website):
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        if messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {email} " f"\nPassword: {password} \nIs it ok to save?"):
            save_json_file(new_data)
            pyperclip.copy(password)
            messagebox.showinfo(title="Success!", message="The password was copied to the clipboard.")
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- SEARCH DATA ------------------------------- #

def search_website(website):
    data = {}
    try:
        with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day29-30-password-manager-project\data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        pass
    else:
        if website in data:
            userdata = data[website]["username/email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website.title(), message=f"Email/Username: {userdata} \nPassword: {password}\nThe password was copied to the clipboard")
        else:
            messagebox.showerror(title="Error.", message=f"No details for ' {website} ' exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file=r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day29-30-password-manager-project\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0,column=1)

website_lb = Label(text="Website:", bg="white")
website_lb.grid(row=1, column=0)
website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command= lambda: search_website(website_entry.get().title()))
search_button.grid(row=1, column=2)

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