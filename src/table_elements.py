
"""Simple Tkinter listbox example."""

import tkinter as tk


def show_selection():
    """Display the selected item in the label."""
    selection = listbox.get(tk.ACTIVE)
    label.config(text=f"You selected: {selection}")


def main():
    global listbox, label

    # Main window configuration
    window = tk.Tk()
    window.title("Listbox Example")
    window.geometry("300x220")

    # Create listbox
    listbox = tk.Listbox(window)

    for i in range(1, 4):
        listbox.insert(tk.END, f"Option {i}")

    listbox.pack()

    # Button to show selection
    button_show = tk.Button(
        window,
        text="Show Selection",
        command=show_selection
    )
    button_show.pack()

    # Label to display selection
    label = tk.Label(window)
    label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
