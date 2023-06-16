import tkinter as tk
from tkinter import ttk

def on_delta_selected(event):
    selected_delta = delta_var.get()
    print("Selected Delta:", selected_delta)

def on_data_type_selected(event):
    selected_data_type = data_type_var.get()
    print("Selected Data Type:", selected_data_type)
    show_sub_menu(selected_data_type)

def show_sub_menu(data_type):
    # Hide all sub-menus
    month_menu.grid_remove()
    strip_menu.grid_remove()
    spread_menu.grid_remove()

    if data_type == "Month":
        month_menu.grid()
    elif data_type == "Strip":
        strip_menu.grid()
    elif data_type == "Spread":
        spread_menu.grid()

def on_month_selected(event):
    selected_month = month_var.get()
    print("Selected Month:", selected_month)

def on_strip_selected(event):
    selected_strip = strip_var.get()
    print("Selected Strip:", selected_strip)

def on_spread_selected(event):
    selected_spread = spread_var.get()
    print("Selected Spread:", selected_spread)

def on_go_button_click():
    print("Go button clicked!")

# Create the main window
window = tk.Tk()
window.title("User Interactive Window")

# Create the Delta drop-down menu
delta_label = tk.Label(window, text="Delta:")
delta_label.pack()

delta_var = tk.StringVar()
delta_dropdown = ttk.Combobox(window, textvariable=delta_var, values=["5 delta", "15 delta", "30 delta"])
delta_dropdown.pack()
delta_dropdown.bind("<<ComboboxSelected>>", on_delta_selected)

# Create the Data Type drop-down menu
data_type_label = tk.Label(window, text="Data Type:")
data_type_label.pack()

data_type_var = tk.StringVar()
data_type_dropdown = ttk.Combobox(window, textvariable=data_type_var, values=["Month", "Strip", "Spread"])
data_type_dropdown.pack()
data_type_dropdown.bind("<<ComboboxSelected>>", on_data_type_selected)

# Create the sub-menus
month_menu = tk.Frame(window)
month_label = tk.Label(month_menu, text="Month:")
month_label.pack()

month_var = tk.StringVar()
month_dropdown = ttk.Combobox(month_menu, textvariable=month_var, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
month_dropdown.pack()
month_dropdown.bind("<<ComboboxSelected>>", on_month_selected)

strip_menu = tk.Frame(window)
strip_label = tk.Label(strip_menu, text="Strip:")
strip_label.pack()

strip_var = tk.StringVar()
strip_dropdown = ttk.Combobox(strip_menu, textvariable=strip_var, values=["Summer", "Winter", "Fall", "Spring"])
strip_dropdown.pack()
strip_dropdown.bind("<<ComboboxSelected>>", on_strip_selected)

spread_menu = tk.Frame(window)
spread_label = tk.Label(spread_menu, text="Spread:")
spread_label.pack()

spread_var = tk.StringVar()
spread_dropdown = ttk.Combobox(spread_menu, textvariable=spread_var, values=["1", "2", "3"])
spread_dropdown.pack()
spread_dropdown.bind("<<ComboboxSelected>>", on_spread_selected)

# Place the sub-menus within the main window
month_menu.place(x=150, y=80)
strip_menu.place(x=150, y=80)
spread_menu.place(x=150, y=80)

# Create the Go button
go_button = tk.Button(window, text="Go", command=on_go_button_click)
go_button.pack()

# Start with all sub-menus hidden
month_menu.grid_remove()
strip_menu.grid_remove()
spread_menu.grid_remove()

# Start the main loop
window.mainloop()
