from tkinter import *
import requests
from classes.WebImg import WebImg

class City:
    def __init__(self, root, geo):
        self.root = root
        # Fetch data from API using geo coordinates
        data = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={geo['lat']}&lon={geo['lon']}", headers={"User-Agent": "Weather App - https://github.com/Pigges/final-project"})
        # Parse response into JSON
        data = data.json()

        # Save units
        self.units = data['properties']['meta']['units']

        # List all measured data periods
        self.periods = []

        for period in data['properties']['timeseries']:
            code = 'n/a'
            if 'next_12_hours' in period['data'].keys():
                code = period['data']['next_12_hours']['summary']['symbol_code']

            self.periods.append({
                "time": period['time'],
                "details": period['data']['instant']['details'],
                "symbol_code": code
            })
        
        #weatherIcon = WebImg(f"https://api.met.no/images/weathericons/svg/{self.periods[0]['symbol_code']}.svg").get()
        #Label(self.root, image=weatherIcon).pack()