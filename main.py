from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import searchCity

root = Tk()

root.title("WeatherApp")
logo = Image.open('logo.ico')
logo = ImageTk.PhotoImage(logo)
root.wm_iconphoto(True, logo)

root.geometry("500x600")

#listbox = Listbox(root)

# Search results
def citySearch():
    searchCity.showResults(root, search_box.get())


header = ttk.Frame(root)
header.pack(pady=10)
ttk.Label(header, text="Lookup weather for").grid(column=0, row=0, padx=10)
search_box = ttk.Entry(header)
search_box.grid(column=1, row=0)
ttk.Button(header, text="Search", command=citySearch).grid(column=2, row=0, padx=10)

root.mainloop()