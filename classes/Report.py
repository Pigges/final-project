from tkinter import *
from utils.file import read
from classes.City import City

class Report:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()
        self.setup()

    def setup(self):
        Button(self.frame, text="Reload", command=self.reload).pack(pady=(5, 20))
        self.report = Frame(self.frame)
        self.report.pack()
        self.list = []
        self.cities = read('./data/cities.json')

        for id in self.cities:
            self.list.append(City(self.report, self.cities[id]))

    def reload(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.setup()