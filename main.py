from StoreUI import window, window_2, window_3
from StoreFunctions import update_labels
window.withdraw()
window_3.withdraw()
# window_3.quit_flag = False
# window_3.protocol("WM_DELETE_WINDOW", lambda: setattr(window, "quit_flag", True))
update_labels()
window.mainloop()
