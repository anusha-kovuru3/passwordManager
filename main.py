from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# PASSWORD GENERATOR

def your_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters = [random.choice(letters) for char in range(nr_letters)]
    symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = letters + symbols + numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


#  SAVE PASSWORD

def save():
    new_data = {
        entry_label.get(): {
            "email": username.get(),
            "password": password_entry.get()
        }
    }
    if entry_label.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title="oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating the new data to the old data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)

        finally:
            entry_label.delete(0, 'end')
            password_entry.delete(0, 'end')


# FINDING PASSWORD


def find_password():
    website = entry_label.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="oops!", message="No Data File Found.")
    else:
        if website in data:
            user_name = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {user_name}\nPassword: {password}")

        else:
            messagebox.showerror(title="Error", message=f"No details of {website} exists.")


#  UI SETUP


window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:", font=("Timer of Roman", 10, "bold"))
website_label.grid(row=1, column=0)

# email/username label
email = Label(text="Email/Username:", font=("Timer of Roman", 10, "bold"))
email.grid(row=2, column=0)

# password label
password_label = Label(text="Password:", font=("Timer of Roman", 10, "bold"))
password_label.grid(row=3, column=0)

# entry label
entry_label = Entry(width=17)
entry_label.focus()
entry_label.grid(row=1, column=1)

# entry label for email/username label
username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2)
username.insert(0, "anushakovuru3@gmail.com")  # pre populated

# password entry
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# generate password button
generate_password = Button(text="Generate Password", command=your_password)
generate_password.grid(row=3, column=2)

# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# search button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
