
"""Program to choose a place to travel"""

import tkinter as tk


def choose_trip():
    option = []

    if beach.get() == 1:
        option.append("Beach")

    if mountain.get() == 1:
        option.append("Mountain")

    if rural_tourism.get() == 1:
        option.append("Rural Tourism")

    places_label.config(text=" ".join(option))


def create_button(text, variable):
    tk.Checkbutton(
        window,
        text=text,
        variable=variable,
        onvalue=1,
        offvalue=0,
        bg="pink",
        command=choose_trip
    ).pack()


# Main window configuration
window = tk.Tk()
window.title("Places to Travel")
window.config(bg="pink")
window.geometry("270x150")
window.resizable(False, False)
window.iconbitmap("../images/plane.ico")

# Variables for travel options
beach = tk.IntVar()
mountain = tk.IntVar()
rural_tourism = tk.IntVar()

# Title label
tk.Label(
    window,
    text="Choose your destination:",
    width=20,
    bg="pink"
).pack(pady=10)

# Create option buttons
create_button("Beach", beach)
create_button("Mountain", mountain)
create_button("Rural Tourism", rural_tourism)

# Label that shows the selected places
places_label = tk.Label(window, bg="pink", pady=10)
places_label.pack(side="bottom")

window.mainloop()
