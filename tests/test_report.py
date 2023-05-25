"""
Tests for Report
"""

import unittest
from tkinter import Tk
from classes.report import Report

class TestReport(unittest.TestCase):
    """
    Tests for Report
    """
    def test_setup(self):
        """
        Test setting up Report
        """
        report = Report(Tk())
        self.assertTrue(report.reload())
