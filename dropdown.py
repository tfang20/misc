import tkinter as tk
from tkinter import ttk

def on_delta_selected(event):
    selected_delta = delta_var.get()
    print("Selected Delta:", selected_delta)

def on_data_type_selected(event):
    selected_data_type = data_type_var.get()
    print("Selected Data Type:", selected_data_type)

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
data_type_dropdown = ttk.Combobox(window, textvariable=data_type_var, values=["Data Type 1", "Data Type 2", "Data Type 3"])
data_type_dropdown.pack()
data_type_dropdown.bind("<<ComboboxSelected>>", on_data_type_selected)

# Create the Go button
go_button = tk.Button(window, text="Go", command=on_go_button_click)
go_button.pack()

# Start the main loop
window.mainloop()
