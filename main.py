"""
Main file for the weather app
"""

# Make imports
from tkinter import ttk, Tk
from PIL import ImageTk, Image
from classes.report import Report
from header import create_header

# Initialize the Tkinter instance
root = Tk()

# Set window title and logo
root.title("WeatherApp")
logo = Image.open('logo.ico')
logo = ImageTk.PhotoImage(logo)
root.wm_iconphoto(True, logo)

# Set window size
root.geometry("500x600")

# Create a title, telling the name of the application
ttk.Label(root, text="Weather App", font="bold").pack()

# Call to create Header
create_header(root)

# Call to create the weather Report
Report(root)

# Starting the main loop
root.mainloop()
