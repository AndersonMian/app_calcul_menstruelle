import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Gomycode", )
label.pack()

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

window.mainloop()