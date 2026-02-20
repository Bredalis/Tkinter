
import tkinter as tk


def main():
    """Main function to create the window."""
    
    # Main window configuration
    window = tk.Tk()
    window.title("Hello World")
    window.resizable(False, False)
    window.iconbitmap("../images/python.ico")

    # Greeting label
    greeting_label = tk.Label(
        window,
        text="Hello Programming World",
        fg="#884EA0",
        bg="pink",
        font=("Arial", 25),
        padx=10,
        pady=10
    )
    greeting_label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
