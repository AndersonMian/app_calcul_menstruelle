# Import the tkinter module and alias it as tk
import tkinter as tk
# Define a dictionary that maps string values to relief attributes
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
# Create a Tkinter window
window = tk.Tk()
# Loop through each item in the border_effects dictionary
for relief_name, relief in border_effects.items():
    # Create a new frame widget with the specified relief and border width
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    # Pack the frame widget onto the left side of the window
    frame.pack(side=tk.LEFT)
    # Create a new label widget within the frame, displaying the relief name
    label = tk.Label(master=frame, text=relief_name)
    # Pack the label widget within the frame
    label.pack()
# Enter the Tkinter main event loop
window.mainloop()