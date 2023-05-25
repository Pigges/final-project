"""
Handles the class for a Weather
"""

class Weather:
    """
    Class for a Weather

    Keyword arguments:
    period -- a period of time containing information about the weather
    """
    def __init__(self, period):
        self.time = period['time']
        self.details = period['data']['instant']['details']

        code = 'n/a'
        # Check wether or not we have a symbol_code for the current period
        if 'next_12_hours' in period['data'].keys():
            code = period['data']['next_12_hours']['summary']['symbol_code']

        self.code = code

    def get_time(self):
        """
        Get the time the weather refers to
        """
        return self.time

    def get_details(self):
        """
        Get details of the weather, containing temperatures and more
        """
        return self.details

    def get_code(self):
        """
        Get the weather code
        """
        return self.code
