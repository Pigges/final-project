from tkinter import *
from utils.file import read
from classes.City import City

class Report:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()

        Button(self.frame, text="Reload").pack(anchor="nw")

        self.setup()

    def setup(self):
        self.report = Frame(self.frame)
        self.list = []
        self.cities = read('./data/cities.json')

        for id in self.cities:
            self.list.append(City(self.report, self.cities[id]))