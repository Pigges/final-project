"""
Handles a weather period
"""

class Period:
    """
    Class for a weather period
    """
    def __init__(self, period):
        code = 'n/a'
        # Check wether or not we have a symbol_code for the current period
        if 'next_12_hours' in period['data'].keys():
            code = period['data']['next_12_hours']['summary']['symbol_code']

        self.period = {
            "time": period['time'],
            "details": period['data']['instant']['details'],
            "symbol_code": code
        }

    def get_period(self):
        """
        Retrieves the period
        """
        return self.period
