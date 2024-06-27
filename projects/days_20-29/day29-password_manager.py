# import some libraries

from tkinter import *
from tkinter import messagebox
from data.day29.day29_passwordgeneratormodified import Password
import pyperclip
import json
from json.decoder import JSONDecodeError

# set up the UI

screen = Tk()
screen.config(padx=50, pady=50)
screen.title("Password manager!")


# create the functions that the program will use

def get_info():
    global response
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()

    response = None

    if 0 in [len(website), len(email), len(password)]:
        messagebox.showwarning(title="Empty field", message="Please, be sure that all fields are filled.")
    else:
        response = messagebox.askokcancel(title=f"{website}",
                                          message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nIt is OK to save the data?")

    if response:

        new_data = {website.lower(): {
            "email": email,
            "password": password}
        }

        try:
            with open("data/day29/passwords.json", mode="r") as f:
                password_json = json.load(f)


        except (FileNotFoundError, JSONDecodeError):
            with open("data/day29/passwords.json", mode="w") as f:
                json.dump(new_data, f, indent=4)

        else:
            with open("data/day29/passwords.json", mode="w") as f:
                password_json.update(new_data)
                json.dump(new_data, f, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


def create_password():
    pass_input.delete(0, END)
    new_pass = Password().string_password
    pass_input.insert(0, new_pass)

    pyperclip.copy(new_pass)


def search_web():
    web = website_input.get().lower()

    try:
        with open("data/day29/passwords.json", mode="r") as f:
            password_json = json.load(f)

        web_email = password_json[web]["email"]
        web_password = password_json[web]["password"]

        messagebox.showinfo(title=f"{web.title()}", message=f"Email: {web_email}\nPassword: {web_password}")
    except (KeyError, JSONDecodeError):
        messagebox.showinfo(title=f"{web.title()}", message=f"No credentials were found!")


# create a canvas with an img

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="data/day29/day29_logo.png")
canvas.create_image(136, 100, image=lock_img)
canvas.grid(row=0, column=1)

# create and configure the labels, inputs and buttons

website = Label(text="Website:")
website.grid(row=1, column=0, sticky="e")

website_input = Entry()
website_input.grid(row=1, column=1)
website_input.focus()

website_search = Button(text="Search", width=13, command=search_web)
website_search.grid(row=1, column=2)

email = Label(text="Username/email:")
email.grid(row=2, column=0, sticky='e')

email_input = Entry(width=38)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, string="pedrosergey@example.com")

password = Label(text="Password:")
password.grid(row=3, column=0, sticky="e")

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)

gen_password = Button(text="Generate password", width=13, command=create_password)
gen_password.grid(row=3, column=2)

add_password = Button(text="Save password", width=36, command=get_info)
add_password.grid(row=4, column=1, columnspan=2)

screen.mainloop()
