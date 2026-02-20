
"""Program to choose a gender"""

import tkinter as tk


def main():
    """Main function to create the GUI."""

    # Main window configuration
    window = tk.Tk()
    window.config(bg="pink")
    window.resizable(False, False)
    window.title("Gender Selection")
    window.geometry("270x125")
    window.iconbitmap("../images/gender.ico")

    # Gender options
    option = tk.IntVar()
    genders = ["Male", "Female", "Other"]

    # Label to display the selected gender
    selected_label = tk.Label(window, bg="pink")
    selected_label.pack()

    def choose_gender():
        """Display the selected gender."""
        selection = genders[option.get() - 1]
        selected_label.config(text=f"You selected {selection.lower()}")

    # Title label
    tk.Label(window, text="Gender:", bg="pink", pady=5).pack()

    def create_button(text, value):
        """Create a radio button."""
        tk.Radiobutton(
            window,
            text=text,
            bg="pink",
            activebackground="skyblue",
            variable=option,
            value=value,
            command=choose_gender
        ).pack()

    # Create gender selection buttons
    for i, text in enumerate(genders, start=1):
        create_button(text, i)

    window.mainloop()


if __name__ == "__main__":
    main()
