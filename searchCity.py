from tkinter import *
import requests
from classes.SearchResultBtn import SearchResultBtn

def showResults(root, search):
    window = Toplevel(root)
    resp = fetch(search)

    Label(window, text=f"Found {len(resp)} results for '{search}'").pack()

    buttons = []
    
    for city in resp:
        buttons.append(SearchResultBtn(window, city))


def fetch(q):
    city = requests.get("https://geocode.maps.co/search?q=" + q)
    city = city.json()
    #print(city)
    return city