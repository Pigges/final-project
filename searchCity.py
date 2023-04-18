from tkinter import *
import requests

def showResults(root, search):
    window = Toplevel(root)
    resp = fetch(search)

    #Label(window, text="Search Results!").pack()
    
    for city in resp:
        Button(window, text=city["display_name"], command=lambda: handleSelect(city["display_name"])).pack()


def fetch(q):
    city = requests.get("https://geocode.maps.co/search?q=" + q)
    city = city.json()
    #print(city)
    return city

def handleSelect(city):
    print(city)