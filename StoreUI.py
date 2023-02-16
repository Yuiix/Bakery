from tkinter import Canvas, PhotoImage, Label, Entry, Tk, Button, Toplevel
from PIL import Image, ImageTk
import StoreFunctions

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window_2 = Toplevel(window)
window_3 = Toplevel(window)
window_3.title("Panaderia Plaza Vieja")
window_3.config(padx=50, pady=50, bg="#F4FCD9")
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
canvas_2 = Canvas(window, height=500, width=500, bg="#F4FCD9", highlightthickness=0)
# Load an image in the script
image_2 = (Image.open("bread-g7ad324148_640.jpg"))
resize_image_2 = image_2.resize((400, 300), Image.ANTIALIAS)
new_image_2 = ImageTk.PhotoImage(resize_image_2)
canvas_2.create_image(350, 250, image=new_image_2)
canvas_2.grid(row=0, column=0, columnspan=6)

email_label = Label(window_2, text="Usuario:")
email_label.grid(row=2, column=0)
password_label = Label(window_2, text="Contrasena:")
password_label.grid(row=3, column=0)

email_entry = Entry(window_2, width=24)
email_entry.grid(row=2, column=1)  # columnspan=2)
email_entry.insert(0, "socorro0708")

password_entry = Entry(window_2, width=24)
password_entry.grid(row=3, column=1)

# -------------------------Button's for log in ----------------------
log_button = Button(window_2, text="Entrar", width=36, command=lambda: StoreFunctions.check_user())
log_button.grid(row=4, column=1)  # columnspan=2)

# -------------------------Label's for bread price ----------------------
bread_label_1 = Label(window, text="Precio del Pan #1:")
bread_label_1.grid(row=2, column=0)

bread_label_2 = Label(window, text="Precio del Pan #2:")
bread_label_2.grid(row=3, column=0)

bread_label_3 = Label(window, text="Precio del Pan #3:")
bread_label_3.grid(row=4, column=0)

bread_label_4 = Label(window, text="Precio del Pan #4:")
bread_label_4.grid(row=5, column=0)

# -------------------------Label's for bread quantity ----------------------
bread_label_5 = Label(window, text="Cantidad del Pan #1:")
bread_label_5.grid(row=2, column=2)

bread_label_6 = Label(window, text="Cantidad del Pan #2:")
bread_label_6.grid(row=3, column=2)

bread_label_7 = Label(window, text="Cantidad del Pan #3:")
bread_label_7.grid(row=4, column=2)

bread_label_8 = Label(window, text="Cantidad del Pan #4:")
bread_label_8.grid(row=5, column=2)

bread_label_9 = Label(window, text="Cantidad del Pan extra:")
bread_label_9.grid(row=2, column=5)

# -------------------------Entry's for bread price ----------------------
bread_entry_1 = Entry(window, width=15)
bread_entry_1.grid(row=2, column=1)  # columnspan=2)

bread_entry_2 = Entry(window, width=15)
bread_entry_2.grid(row=3, column=1)  # columnspan=2)

bread_entry_3 = Entry(window, width=15)
bread_entry_3.grid(row=4, column=1)  # columnspan=2)

bread_entry_4 = Entry(window, width=15)
bread_entry_4.grid(row=5, column=1)  # columnspan=2)
# -------------------------Entry's for bread quantity ----------------------
bread_entry_5 = Entry(window, width=15)
bread_entry_5.grid(row=2, column=3)  # columnspan=2)

bread_entry_6 = Entry(window, width=15)
bread_entry_6.grid(row=3, column=3)  # columnspan=2)

bread_entry_7 = Entry(window, width=15)
bread_entry_7.grid(row=4, column=3)  # columnspan=2)

bread_entry_8 = Entry(window, width=15)
bread_entry_8.grid(row=5, column=3)  # columnspan=2)

bread_entry_9 = Entry(window, width=15)
bread_entry_9.grid(row=2, column=6)  # columnspan=2)
# -------------------------Button's for bread quantity ----------------------
exit_button = Button(window, text="Salir", width=15, command=lambda: StoreFunctions.show_again())
exit_button.grid(row=7, column=2)  # columnspan=2)

save_button = Button(window, text="Guardar", width=15, command=lambda: StoreFunctions.save_bread_price())
save_button.grid(row=7, column=1)  # columnspan=2)

add_extra_bread_button = Button(window, text="Añadir el pan extra", width=15, command=lambda: StoreFunctions.save_bread_price())
add_extra_bread_button.grid(row=3, column=6)  # columnspan=2)
# Dummy commit 6
# TO DO create the json with the date name
# TO DO include the total of bread and prices of that day into the json file
# TO DO include the total of bread sold, left and total money of the day
# TO DO check if that json file already exist and if you want to override it
