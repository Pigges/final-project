import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen


# Reference: https://stackoverflow.com/questions/65635835/displaying-image-from-url-in-python-tkinter
class WebImg:
    def __init__(self,url):
        u = urlopen(url)
        raw_data = u.read()
        u.close()

        self.image = ImageTk.PhotoImage(data=raw_data) # <-----

    def get(self):
        return self.image