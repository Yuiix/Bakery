from StoreUI import window, window_2, window_4, window_3, window_5, icon_path
from StoreFunctions import update_labels

window.withdraw()
window_3.withdraw()
window_4.withdraw()
window_5.withdraw()
update_labels()
window.iconbitmap(icon_path)
window_2.iconbitmap(icon_path)
window_3.iconbitmap(icon_path)
window_4.iconbitmap(icon_path)
window_5.iconbitmap(icon_path)
window.mainloop()
