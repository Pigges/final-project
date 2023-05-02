from tkinter import *
from utils.file import read, write

class SearchResultBtn:
    def __init__(self, root, city):
        self.city = city
        self.root = root
        but = Button(root, text=self.city["display_name"], command=self.handleSelect)
        but.pack(pady=5)


    def handleSelect(self):
        print(self.city["display_name"])
        cities = read('./data/cities.json')
        cities[self.city["place_id"]] = self.city
        write('./data/cities.json', cities)
        self.root.destroy()