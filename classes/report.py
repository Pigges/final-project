"""
Handle the Report list
"""

from tkinter import ttk
from utils.file import read
from classes.city import City

class Report:
    """
    Class for the Report
    """
    def __init__(self, root):
        self.frame = ttk.Frame(root)
        self.frame.pack()
        self.setup()

    def setup(self):
        """
        Set up the Report and fetch everything
        """
        ttk.Button(self.frame, text="Reload", command=self.reload).pack(pady=(5, 20))
        self.report = ttk.Frame(self.frame)
        self.report.pack()
        self.list = []
        self.cities = read('./data/cities.json')

        for id_ in self.cities:
            self.list.append(City(self.report, self.cities[id_]))

    def reload(self):
        """
        Reload Report by clearing it and fetching everything again
        """
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.setup()
