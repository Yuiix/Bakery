from tkinter import Canvas, Label, Entry, Tk, Button, Toplevel, Frame, Menu, OptionMenu, StringVar, \
    messagebox
from PIL import Image, ImageTk
import StoreFunctions
import json
from datetime import date
from FileCreator import create_files_with_sells

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window_2 = Toplevel()
window_3 = Toplevel()
window_4 = Toplevel()
window_4.title("Panaderia Plaza Vieja")
window_4.config(padx=50, pady=50, bg="#ECF9FF")
window_3.title("Panaderia Plaza Vieja")
window_3.config(padx=50, pady=50, bg="#ECF9FF")
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
# canvas_2 = Canvas(window, height=600, width=600, bg="#F4FCD9", highlightthickness=0)
# Load an image in the script
# image_2 = (Image.open("bread-g7ad324148_640.jpg"))
# resize_image_2 = image_2.resize((300, 300), Image.ANTIALIAS)
# new_image_2 = ImageTk.PhotoImage(resize_image_2)
# canvas_2.create_image(300, 300, image=new_image_2)
# canvas_2.grid(row=0, column=0, columnspan=6)
# ------------------------- Canvas set up for hird Window -------------#
canvas_3 = Canvas(window_3, height=400, width=400, bg="#FEFBE9", highlightthickness=0)
# Load an image in the script
image_3 = (Image.open("breads-g518892b9c_1920.jpg"))
resize_image_3 = image_3.resize((400, 400), Image.ANTIALIAS)
new_image_3 = ImageTk.PhotoImage(resize_image_3)
canvas_3.create_image(200, 200, image=new_image_3)
canvas_3.grid(row=0, column=0, columnspan=1)

# ------------------------- Frame creation for Third window -----------
menu_frame = Frame(window_3, bg='#FFFBEB')
menu_frame.grid(row=0, column=1, sticky='ns')
menu = Menu(window_3)
window_3.config(menu=menu)
# ##-----------------------------------------------
email_label = Label(window_2, text="Usuario:")
email_label.grid(row=2, column=0)
password_label = Label(window_2, text="Contrasena:")
password_label.grid(row=3, column=0)

email_entry = Entry(window_2, width=24)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "socorro0708")

password_entry = Entry(window_2, width=24)
password_entry.grid(row=3, column=1)

# -------------------------Button's for log in ----------------------
log_button = Button(window_2, text="Entrar", width=36, command=lambda: StoreFunctions.check_user())
log_button.grid(row=4, column=1)

# -------------------------Label's for bread price -------------------------
for o in range(1, 5):
    bread_label_prices = Label(window, text="Precio del Pan #" + str(o))
    bread_label_prices.grid(row=o + 1, column=0)

# -------------------------Label's for bread quantity ------------------------------------
for n in range(1, 5):
    bread_label_quantity = Label(window, text="Cantidad del Pan #" + str(n))
    bread_label_quantity.grid(row=n + 1, column=2, padx=5, pady=5)
    # -------------------------Label's for EXTRA bread quantity ------------------------------------
for n in range(1, 5):
    bread_label_quantity = Label(window, text="Cantidad del Pan extra #" + str(n))
    bread_label_quantity.grid(row=n + 1, column=5, padx=5, pady=5)

# -------------------------Label's for the name of the file to save the ticket ----------------------
bread_label_file = Label(window, text="Nombre del Archivo:")
bread_label_file.grid(row=7, column=5)

# -------------------------Label's for bread sells ------------------------
for i in range(1, 5):
    bread_label_sell = Label(menu_frame, text="Cantidad a vender del Pan #" + str(i))
    bread_label_sell.config(bg="#FFE7CC")
    bread_label_sell.grid(row=i, column=1, padx=10, pady=10)

bread_label_14 = Label(menu_frame, text="Total a cobrar")
bread_label_14.config(bg="#FFE7CC")
bread_label_14.grid(row=5, column=1, padx=10, pady=10)
# -------------------------Label's for bread sells price ----------------------
try:
    with open("data.json") as data_file:
        data = json.load(data_file)
        bread_sell_labels = []
        for i in range(1, 5):
            label_with_price = Label(menu_frame, text="x " + data["bread_prices"]["bread_price_" + str(i)])
            label_with_price.config(bg="#FFE7CC")
            label_with_price.grid(row=i, column=4, padx=10, pady=10)
            # ------ List to update in the store functions---------------------
            bread_sell_labels.append(label_with_price)
except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found.")
# ------------------------- Label which contains the total to charge -----------
bread_label_total = Label(menu_frame, text="0")
bread_label_total.config(bg="#FFE7CC")
bread_label_total.grid(row=5, column=6, padx=10, pady=10)
# -------------------------Label's for distribution bread ------------------------
for i in range(1, 5):
    bread_label_distribution = Label(window_4, text="Cantidad a repartir del pan #" + str(i))
    bread_label_distribution.config(bg="#FFE7CC")
    bread_label_distribution.grid(row=i+1, column=1, padx=10, pady=10)
# -------------------------Entry's for bread price ------------------------------
bread_entry_1 = Entry(window, width=15)
bread_entry_1.grid(row=2, column=1)

bread_entry_2 = Entry(window, width=15)
bread_entry_2.grid(row=3, column=1)

bread_entry_3 = Entry(window, width=15)
bread_entry_3.grid(row=4, column=1)

bread_entry_4 = Entry(window, width=15)
bread_entry_4.grid(row=5, column=1)
# -------------------------Entry's for bread quantity ----------------------
bread_entry_5 = Entry(window, width=15)
bread_entry_5.grid(row=2, column=3)

bread_entry_6 = Entry(window, width=15)
bread_entry_6.grid(row=3, column=3)

bread_entry_7 = Entry(window, width=15)
bread_entry_7.grid(row=4, column=3)

bread_entry_8 = Entry(window, width=15)
bread_entry_8.grid(row=5, column=3)

# -------------------------Entry's for EXTRA bread quantity ----------------------
extra_bread_entry = []
for x in range(1, 5):
    # quantity_options = [str(i) for i in range(0, 11)]
    bread_entry_extra = Entry(window, width=15)
    extra_bread_entry.append(bread_entry_extra)
    bread_entry_extra.grid(row=x + 1, column=6, padx=5, pady=5)
# -------------------------Entry's for distribute bread  ----------------------
distribute_bread_entry = []
for x in range(1, 5):
    bread_entry_distribute = Entry(window_4, width=15)
    distribute_bread_entry.append(bread_entry_distribute)
    bread_entry_distribute.grid(row=x + 1, column=2, padx=5, pady=5)
# -------------------------Entry's for the name of the file ------------------------
bread_entry_file = Entry(window, width=15)
bread_entry_file.grid(row=7, column=6)
# get the current date and format it as YYYY-MM-DD
bread_entry_file.insert(0, date.today().strftime("%Y-%m-%d"))
# -------------------------Entry's for the bread sell ------------------------
# Create a list to store the selected options
selected_options = [StringVar() for i in range(6)]
# Set the initial values of the selected options
for i in range(6):
    selected_options[i].set("0")
for x in range(1, 5):
    quantity_options = [str(i) for i in range(0, 11)]
    quantity_dropdown = OptionMenu(menu_frame, selected_options[x], *quantity_options)
    quantity_dropdown.grid(row=x, column=3)
# ---------------------------- Label with the final price after multiply --------------------------------------
try:
    with open("data.json") as data_file:
        data = json.load(data_file)
        bread_multiply_labels = []
        for i in range(1, 5):
            label_with_multiply = Label(menu_frame,
                                        text=(str(float(data["bread_prices"]["bread_price_" + str(i)]) *
                                                  float(selected_options[i].get()))))
            label_with_multiply.grid(row=i, column=6, padx=10, pady=10)
            label_with_multiply.config(bg="#FFE7CC")
            bread_multiply_labels.append(label_with_multiply)
except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found.")
# -------------------------Button's for bread quantity ----------------------
exit_button = Button(window, text="Salir", width=15, command=lambda: StoreFunctions.show_again())
exit_button.grid(row=7, column=2)

save_button = Button(window, text="Guardar", width=15, command=lambda: StoreFunctions.save_bread_price())
save_button.grid(row=7, column=1)

# -------------------------Button's for extra bread quantity ----------------------
add_extra_bread_button = Button(window, text="Añadir el pan extra", width=15,
                                command=lambda: StoreFunctions.extra_bread_function())
add_extra_bread_button.grid(row=2, column=7)
# -------------------------Button's to get the ticket of the day -------------------
obtain_bread_tickets_button = Button(window, text="Obtener tickets", width=15,
                                     command=lambda: create_files_with_sells())
obtain_bread_tickets_button.grid(row=7, column=7)
# -------------------------Button's for bread sells --------------------------------
button_for_sell = Button(menu_frame, text="Vender", width=15,
                         command=lambda: StoreFunctions.sell())
button_for_sell.grid(row=8, column=6)

# -------------------------Button's for exit --------------------------------------
exit_button_for_sells = Button(menu_frame, text="Salir", width=15,
                               command=lambda: StoreFunctions.show_again())
exit_button_for_sells.grid(row=8, column=1)

exit_button_for_distribution = Button(window_4, text="Salir", width=15,
                                      command=lambda: StoreFunctions.hide_distribution())
exit_button_for_distribution.grid(row=6, column=1)

# -------------------------Button's for distribute bread --------------------------------------
distribute_bread_button = Button(menu_frame, text="Pan para repartir", width=15,
                                 command=lambda: StoreFunctions.show_distribution())
distribute_bread_button.grid(row=9, column=1, padx=10, pady=10)

exit_button_for_distribution = Button(window_4, text="Quitar pan", width=15,
                                      command=lambda: StoreFunctions.hide_distribution())
exit_button_for_distribution.grid(row=6, column=2)
