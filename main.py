from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()

root.title("WeatherApp")
logo = Image.open('logo.ico')
logo = ImageTk.PhotoImage(logo)
root.wm_iconphoto(True, logo)

root.geometry("500x600")

# Search results
results = ttk.Frame(root)
results.grid(column=0, row=1)
searchTitle = ttk.Label(results, text="Search results")
def citySearch():
    print(search_box.get())
    searchTitle.grid_forget()
    searchTitle.grid()

header = ttk.Frame(root, padding=10)
header.grid(column=0, row=0)
ttk.Label(header, text="Lookup weather for").grid(column=0, row=0)
search_box = ttk.Entry(header)
search_box.grid(column=1, row=0)
ttk.Button(header, text="Search", command=citySearch).grid(column=2, row=0)

root.mainloop()