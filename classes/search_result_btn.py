"""
Handle the Button for a city result
"""

from tkinter import ttk
from utils.file import read, write

class SearchResultBtn:
    """
    Class for the search result button

    Keyword arguments:
    root -- the master tkinter frame
    city -- dictionary containing information about the city
    """
    def __init__(self, root, city):
        self.city = city
        self.root = root
        button = ttk.Button(root, text=self.city["display_name"], command=self.handle_select)
        button.pack(pady=5)


    def handle_select(self):
        """
        Handle when button is being pressed
        """
        print(self.city["display_name"])
        cities = read('./data/cities.json')
        cities[self.city["place_id"]] = self.city
        write('./data/cities.json', cities)
        self.destroy()

    def destroy(self):
        """
        Destroy the window
        """
        self.root.destroy()
