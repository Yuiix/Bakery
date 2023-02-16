from tkinter import *
from tkinter import messagebox
import json
import StoreUI


def show_again():
    StoreUI.window_2.update()
    StoreUI.window_2.deiconify()
    StoreUI.window.withdraw()
    # StoreUI.window.deiconify()


def save_bread_price():
    bread_data = {
        "bread_prices": {
            "bread_price_1": StoreUI.bread_entry_1.get(),
            "bread_price_2": StoreUI.bread_entry_2.get(),
            "bread_price_3": StoreUI.bread_entry_3.get(),
            "bread_price_4": StoreUI.bread_entry_4.get(),
        },
        "bread_quantities": {
            "bread_quantity_1": StoreUI.bread_entry_5.get(),
            "bread_quantity_2": StoreUI.bread_entry_6.get(),
            "bread_quantity_3": StoreUI.bread_entry_7.get(),
            "bread_quantity_4": StoreUI.bread_entry_8.get(),
            "bread_quantity_5": StoreUI.bread_entry_9.get(),
        }
    }

    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        print("There is no data")
    else:
        # Updating old data with new data
        data.update(bread_data)
        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
            StoreUI.window.update()


def check_user():
    user = StoreUI.email_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if user in data:
            password = data[user]["password"]
            if StoreUI.password_entry.get() == password and user == "socorro0708":
                messagebox.showinfo(title=user, message=f"Welcome to a new day of sales")
                StoreUI.window_2.withdraw()
                entries = [StoreUI.bread_entry_1, StoreUI.bread_entry_2, StoreUI.bread_entry_3, StoreUI.bread_entry_4,
                           StoreUI.bread_entry_5, StoreUI.bread_entry_6, StoreUI.bread_entry_7, StoreUI.bread_entry_8,
                           StoreUI.bread_entry_9]
                for x, i in enumerate(entries):
                    i.delete(0, END)
                    if x <= 3:
                        i.insert(0, data["bread_prices"]["bread_price_" + str(x + 1)])
                    else:
                        i.insert(0, data["bread_quantities"]["bread_quantity_" + str(x - 3)])
                StoreUI.window.deiconify()
            elif StoreUI.password_entry.get() == password and user == "socorro070808":
                print("Hello")
                StoreUI.window_2.withdraw()
                StoreUI.window.withdraw()
                StoreUI.window_3.deiconify()
            else:
                messagebox.showinfo(title="Error", message=f"La contrasena es incorrecta")
        else:
            messagebox.showinfo(title="Error", message=f"El usuario {user} no existe.")
