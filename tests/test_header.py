"""
Tests for Header
"""

import unittest
from tkinter import Tk
from header import city_search, create_header

class TestReport(unittest.TestCase):
    """
    Tests for Header
    """
    def test_setup(self):
        """
        Test setting up Header
        """
        self.assertTrue(create_header(Tk()))
        self.assertTrue(city_search(Tk(), "Stockholm"))
