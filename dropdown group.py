import tkinter as tk
from tkinter import ttk

def on_go_button_click():
    selected_delta = delta_var.get()
    selected_data_type = data_type_tree.item(data_type_tree.focus())['text']
    if selected_delta and selected_data_type:
        selected_options = [selected_delta, selected_data_type]
        print("Selected Options:", selected_options)
        window.destroy()
    
    
        
def on_delta_selected(event):
    selected_delta = delta_var.get()
    print("Selected Delta:", selected_delta)

def on_data_type_selected(event):
    selected_data_type = data_type_tree.item(data_type_tree.focus())['text']
    if selected_data_type not in ['Month', 'Strip', 'Spread']:
        print("Selected Data Type:", selected_data_type)

def on_data_type_click(event):
    selected_data_type = data_type_tree.item(data_type_tree.focus())['text']
    if selected_data_type in ['Month', 'Strip', 'Spread']:
        data_type_tree.selection_remove(data_type_tree.focus())



# Create the main window
window = tk.Tk()
window.title("User Interactive Window")
window.geometry('350x350')

# Create the Delta drop-down menu
delta_label = tk.Label(window, text="Delta:")
delta_label.pack()

delta_var = tk.StringVar()
delta_dropdown = ttk.Combobox(window, textvariable=delta_var, values=["5 delta", "15 delta", "30 delta"], state='readonly')
delta_dropdown.pack()
delta_dropdown.bind("<<ComboboxSelected>>", on_delta_selected)

# Create the Data Type drop-down menu
data_type_label = tk.Label(window, text="Data Type:")
data_type_label.pack()

data_type_var = tk.StringVar()
data_type_tree = ttk.Treeview(window, selectmode='browse')
data_type_tree.pack()

data_type_tree.tag_configure('group', font='TkDefaultFont 9 bold')
data_type_tree.tag_bind('group', '<Button-1>', on_data_type_click)

data_type_tree.insert("", "end", text="Month", tags=('group',))
data_type_tree.insert("", "end", text="Jan", values=("Month",))
data_type_tree.insert("", "end", text="Feb", values=("Month",))
data_type_tree.insert("", "end", text="Mar", values=("Month",))
# Add the rest of the months

data_type_tree.insert("", "end", text="Strip", tags=('group',))
data_type_tree.insert("", "end", text="Spring", values=("Strip",))
data_type_tree.insert("", "end", text="Summer", values=("Strip",))
data_type_tree.insert("", "end", text="Autumn", values=("Strip",))
data_type_tree.insert("", "end", text="Winter", values=("Strip",))

data_type_tree.insert("", "end", text="Spread", tags=('group',))
data_type_tree.insert("", "end", text="1", values=("Spread",))
data_type_tree.insert("", "end", text="2", values=("Spread",))
data_type_tree.insert("", "end", text="3", values=("Spread",))
data_type_scrollbar = ttk.Scrollbar(window, orient="vertical", command=data_type_tree.yview)
data_type_tree.configure(yscrollcommand=data_type_scrollbar.set)
data_type_scrollbar.pack(side="right", fill="y")

data_type_tree.bind("<<TreeviewSelect>>", on_data_type_selected)

# Create the Go button
go_button = tk.Button(window, text="Go", command=on_go_button_click)
go_button.pack()

# Start the main loop
window.mainloop()


