# Assignment 3.py
# Course: IT3883/section W02
# Student Name: Samuel Ekema
# Assignment Number: Lab3
# Due Date: 02/23/2025
# Purpose: Create a GUI application to convert Miles per Gallon into Kilometers per Liter
""" I watched Youtube videos, used geeks.com, w3schools.com as well as stackoverflow to help me complete this project."""


# import the tkinter module
import tkinter as tk

# Conversion factor
MPG_TO_KMPL = 0.425143707



# function to convert mpg to kmpl
def convert_mpg_to_kmpl(event):
    try:
        # Get the users input
        mpg_value = float(entry.get())
        # calculate the conversion
        kmpl_value = mpg_value * MPG_TO_KMPL
        # Display the result
        result_label.config(text=f"{kmpl_value:.2f} km/l")
    except ValueError:
        # Handle non-numeric input so users can get feedback on wrong input
        result_label.config(text="Invalid Input")

# Create tkinter main window
root = tk.Tk()
root.title("MPG to KMPL Converter")
root.geometry("300x150")

# Create label and input field....used youtube for this part. I couldnt figure it out.
tk.Label(root, text="Enter MPG:").pack(pady=5)
entry = tk.Entry(root)
entry.pack()
# Bind input field to function
entry.bind("<KeyRelease>", convert_mpg_to_kmpl)

# Label to display result
result_label = tk.Label(root, text="0.00 km/l", font=("Arial", 14))
result_label.pack(pady=10)

# Run application
root.mainloop()


