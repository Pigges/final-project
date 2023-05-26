"""
Handles the Header Frame
"""

from tkinter import ttk
import search_city

# Search results
def city_search(root, search_box):
    """
    Call search_city to make a city search

    Keyword arguments:
    root -- the master tkinter frame
    search_box -- the search_box
    """
    search_box.delete(0) # Clear search box field
    search_city.show_results(root, search_box.get())
    return True

# Set up the Header Frame
def create_header(root):
    """
    Creating the Header Frame

    Keyword arguments:
    root -- the master tkinter frame
    """
    header = ttk.Frame(root)
    header.pack(pady=10)
    ttk.Label(header, text="Lookup weather for").grid(column=0, row=0, padx=10)
    search_box = ttk.Entry(header)
    search_box.grid(column=1, row=0)
    search = ttk.Button(header, text="Search", command=lambda: city_search(root, search_box))
    search.grid(column=2, row=0, padx=10)
    return True
