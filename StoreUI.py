from tkinter import Canvas, PhotoImage, Label, Entry, Tk, Button, Toplevel
from PIL import Image, ImageTk

import StoreFunctions

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window_2 = Toplevel()
window_2.title("Panaderia Plaza Vieja")
window_2.config(padx=50, pady=50, bg="#F4FCD9")
window.title("Panaderia Plaza Vieja")
window.config(padx=50, pady=50, bg="#F4FCD9")

canvas = Canvas(window_2, height=400, width=400, bg="#F4FCD9", highlightthickness=0)
# Load an image in the script
image = (Image.open("rsz_bread-removebg-preview.png"))
resize_image = image.resize((300, 200), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resize_image)
# logo_img = PhotoImage(file="new_image")

canvas.create_image(200, 200, image=new_image)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
email_label = Label(window_2, text="Usuario:")
email_label.grid(row=2, column=0)
password_label = Label(window_2, text="Contrasena:")
password_label.grid(row=3, column=0)

# Entries
# website_entry = Entry(width=24)
# website_entry.grid(row=1, column=1)
# website_entry.focus()
email_entry = Entry(window_2, width=24)
email_entry.grid(row=2, column=1)  # columnspan=2)
email_entry.insert(0, "Socorro0708")
password_entry = Entry(window_2, width=24)
password_entry.grid(row=3, column=1)

# Buttons
# search_button = Button(text="Search", width=13, command=lambda: StoreFunctions.find_password())
# search_button.grid(row=1, column=2)
# generate_password_button = Button(text="Generate Password", command=lambda: StoreFunctions.generate_password())
# generate_password_button.grid(row=3, column=2)
add_button = Button(window_2, text="Entrar", width=36, command=lambda: StoreFunctions.check_user())
add_button.grid(row=4, column=1)  # columnspan=2)

add_button = Button(text="WUPS", width=36)
add_button.grid(row=0, column=0)  # columnspan=2)
