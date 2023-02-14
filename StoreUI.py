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

# ------------------------- Canvas set up for Main Window -------------#
canvas = Canvas(window_2, height=400, width=400, bg="#F4FCD9", highlightthickness=0)
# Load an image in the script
image = (Image.open("dough-g6d0913849_1920.jpg"))
resize_image = image.resize((300, 200), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resize_image)
canvas.create_image(200, 200, image=new_image)
canvas.grid(row=0, column=0, columnspan=3)
# ------------------------- Canvas set up for Second Window -------------#
canvas_2 = Canvas(window, height=400, width=400, bg="#F4FCD9", highlightthickness=0)
# Load an image in the script
image_2 = (Image.open("bread-g7ad324148_640.jpg"))
resize_image_2 = image_2.resize((300, 200), Image.ANTIALIAS)
new_image_2 = ImageTk.PhotoImage(resize_image_2)
canvas_2.create_image(200, 200, image=new_image_2)
canvas_2.grid(row=0, column=0, columnspan=3)

email_label = Label(window_2, text="Usuario:")
email_label.grid(row=2, column=0)
password_label = Label(window_2, text="Contrasena:")
password_label.grid(row=3, column=0)

email_entry = Entry(window_2, width=24)
email_entry.grid(row=2, column=1)  # columnspan=2)
email_entry.insert(0, "socorro0708")

password_entry = Entry(window_2, width=24)
password_entry.grid(row=3, column=1)

log_button = Button(window_2, text="Entrar", width=36, command=lambda: StoreFunctions.check_user())
log_button.grid(row=4, column=1)  # columnspan=2)

# -------------------------Buttons and entry's for bread entry ----------------------
bread_label_1 = Label(window, text="Precio del Pan #1:")
bread_label_1.grid(row=2, column=0)

bread_label_2 = Label(window, text="Precio del Pan #2:")
bread_label_2.grid(row=3, column=0)

bread_label_3 = Label(window, text="Precio del Pan #3:")
bread_label_3.grid(row=4, column=0)

bread_label_4 = Label(window, text="Precio del Pan #4:")
bread_label_4.grid(row=5, column=0)

bread_entry_1 = Entry(window, width=24)
bread_entry_1.grid(row=2, column=1)  # columnspan=2)
bread_entry_1.insert(0, "2.5")

bread_entry_2 = Entry(window, width=24)
bread_entry_2.grid(row=3, column=1)  # columnspan=2)
bread_entry_2.insert(0, "2.5")

bread_entry_3 = Entry(window, width=24)
bread_entry_3.grid(row=4, column=1)  # columnspan=2)
bread_entry_3.insert(0, "2.5")

bread_entry_4 = Entry(window, width=24)
bread_entry_4.grid(row=5, column=1)  # columnspan=2)
bread_entry_4.insert(0, "2.5")

exit_button = Button(window, text="Salir", width=36, command=lambda: StoreFunctions.show_again())
exit_button.grid(row=6, column=2)  # columnspan=2)

save_button = Button(window, text="Guardar", width=36, command=lambda: StoreFunctions.save_bread_price())
save_button.grid(row=6, column=1)  # columnspan=2)
