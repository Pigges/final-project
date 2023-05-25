"""
Tests for City
"""

import unittest
from tkinter import Tk
from classes.city import City

class TestCity(unittest.TestCase):
    """
    Tests for City
    """
    def test_setup(self):
        """
        Test setting up City
        """
        # Create instance
        city = City(Tk(), {"place_id": 0, "lat": "59", "lon": "18", "display_name": "Stockholm"})
        # Do we have units?
        self.assertEqual(type(city.units), dict)
        # Do we have any periods?
        self.assertEqual(len(city.periods) > 0, True)
        # Can we fetch the weather?
        self.assertEqual(type(city.fetch_weather({"lat": "59", "lon": "18"})), dict)
