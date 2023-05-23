"""
Handles window for city search
"""

from tkinter import ttk, Toplevel
import requests
from classes.search_result_btn import SearchResultBtn

def show_results(root, query):
    """
    Creates and shows city results in a new window

    Keyword arguments:
    root -- the master tkinter frame
    query -- the search query
    """
    window = Toplevel(root)
    resp = fetch(query)

    ttk.Label(window, text=f"Found {len(resp)} results for '{query}'").pack()

    buttons = []

    for city in resp:
        buttons.append(SearchResultBtn(window, city))


def fetch(query):
    """
    Fetches cities and geographical information based on the query

    Keyword arguments:
    query -- the search query
    """
    city = requests.get("https://geocode.maps.co/search?q=" + query, timeout=5)
    city = city.json()
    #print(city)
    return city
