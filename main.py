from tkinter import *
from PIL import ImageTk, Image
from classes.Report import Report
from header import createHeader

root = Tk()

root.title("WeatherApp")
logo = Image.open('logo.ico')
logo = ImageTk.PhotoImage(logo)
root.wm_iconphoto(True, logo)

root.geometry("500x600")

Label(root, text="Weather App", font="bold").pack()

createHeader(root)

Report(root)

root.mainloop()