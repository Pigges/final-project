"""
Handles a weather period
"""

from classes.weather import Weather

class Period(Weather):
    """
    Class for a weather period
    """
    def __init__(self, period):
        Weather.__init__(self, period)
