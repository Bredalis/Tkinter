
import tkinter as tk
from tkinter import ttk


def add_item():
    value = entry.get()
    tree_list.insert("", tk.END, values=(value,))


# Main window configuration
window = tk.Tk()
window.title("Treeview List")
window.geometry("280x330")
window.resizable(False, False)

# Entry to input the element
entry = ttk.Entry(window, width=30)
entry.pack(pady=10)

# Button to add elements
add_button = ttk.Button(
    window,
    text="Add item",
    command=add_item
)
add_button.pack(pady=5)

# Create Treeview to display elements
tree_list = ttk.Treeview(window, columns=("Item",), show="headings")
tree_list.heading("Item", text="Item")
tree_list.pack()

window.mainloop()
