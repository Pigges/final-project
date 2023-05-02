from tkinter import *
import searchCity

# Search results
def citySearch(root, q):
    searchCity.showResults(root, q)

def createHeader(root):
    header = Frame(root)
    header.pack(pady=10)
    Label(header, text="Lookup weather for").grid(column=0, row=0, padx=10)
    search_box = Entry(header)
    search_box.grid(column=1, row=0)
    Button(header, text="Search", command=lambda: citySearch(root, search_box.get())).grid(column=2, row=0, padx=10)