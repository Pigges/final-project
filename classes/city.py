"""
Handle the City weather report
"""

from tkinter import ttk, Frame, Label, Button
import requests

from utils.file import write, read
from classes.period import Period

# Dictionary of all weather types
strings = {
    'clearsky_day': 'Clear Sky Day',
    'clearsky_night': 'Clear Sky Night',
    'clearsky_polartwilight': 'Clear Sky Polar Twilight',
    'fair_day': 'Fair Day',
    'fair_night': 'Fair Night',
    'fair_polartwilight': 'Fair Polar Twilight',
    'partlycloudy_day': 'Partly Cloudy Day',
    'partlycloudy_night': 'Partly Cloudy Night',
    'partlycloudy_polartwilight': 'Partly Cloudy Polar Twilight',
    'cloudy': 'Cloudy',
    'rainshowers_day': 'Rain Showers Day',
    'rainshowers_night': 'Rain Showers Night',
    'rainshowers_polartwilight': 'Rain Showers Polar Twilight',
    'rainshowersandthunder_day': 'Rain Showers And Thunder Day',
    'rainshowersandthunder_night': 'Rain Showers And Thunder Night',
    'rainshowersandthunder_polartwilight': 'Rain Showers And Thunder Polar Twilight',
    'sleetshowers_day': 'Sleet Showers Day',
    'sleetshowers_night': 'Sleet Showers Night',
    'sleetshowers_polartwilight': 'Sleet Showers Polar Twilight',
    'snowshowers_day': 'Snow Showers Day',
    'snowshowers_night': 'Snow Showers Night',
    'snowshowers_polartwilight': 'Snow Showers Polar Twilight',
    'rain': 'Rain',
    'heavyrain': 'Heavy Rain',
    'heavyrainandthunder': 'Heavy Rain And Thunder',
    'sleet': 'Sleet',
    'snow': 'Snow',
    'snowandthunder': 'Snow And Thunder',
    'fog': 'Fog',
    'sleetshowersandthunder_day': 'Sleet Ahowers And Thunder Day',
    'sleetshowersandthunder_night': 'Sleet Ahowers And Thunder Night',
    'sleetshowersandthunder_polartwilight': 'Sleet Ahowers And Thunder Polar Twilight',
    'snowshowersandthunder_day': 'Snow Showers And Thunder Day',
    'snowshowersandthunder_night': 'Snow Showers And Thunder Night',
    'snowshowersandthunder_polartwilight': 'Snow Showers And Thunder Polar Twilight',
    'rainandthunder': 'Rain And Thunder',
    'sleetandthunder': 'Sleet And Thunder',
    'lightrainshowersandthunder_day': 'Light Rain Showers And Thunder Day',
    'lightrainshowersandthunder_night': 'Light Rain Showers And Thunder Night',
    'lightrainshowersandthunder_polartwilight': 'Light Rain Showers And Thunder Polar Twilight',
    'heavyrainshowersandthunder_day': 'Heavy Rain Showers And Thunder Day',
    'heavyrainshowersandthunder_night': 'Heavy Rain Showers And Thunder Night',
    'heavyrainshowersandthunder_polartwilight': 'Heavy Rain Showers And Thunder Polar Twilight',
    'lightssleetshowersandthunder_day': 'Light Sleet Showers And Thunder Day',
    'lightssleetshowersandthunder_night': 'Light Sleet Showers And Thunder Night',
    'lightssleetshowersandthunder_polartwilight': 'Light Sleet Showers And Thunder Polar Twilight',
    'heavysleetshowersandthunder_day': 'Heavy Sleet Showers And Thunder Day',
    'heavysleetshowersandthunder_night': 'Heavy Sleet Showers And Thunder Night',
    'heavysleetshowersandthunder_polartwilight': 'Heavy Sleet Showers And Thunder Polar Twilight',
    'lightssnowshowersandthunder_day': 'Light Snow Showers And Thunder Day',
    'lightssnowshowersandthunder_night': 'Light Snow Showers And Thunder Night',
    'lightssnowshowersandthunder_polartwilight': 'Light Snow Showers And Thunder Polar Twilight',
    'heavysnowshowersandthunder_day': 'Heavy Snow Showers And Thunder Day',
    'heavysnowshowersandthunder_night': 'Heavy Snow Showers And Thunder Night',
    'heavysnowshowersandthunder_polartwilight': 'Heavy Snow Showers And Thunder Polar Twilight',
    'lightrainandthunder': 'Light Rain And Thunder',
    'lightsleetandthunder': 'Light Sleet And Thunder',
    'heavysleetandthunder': 'Heavy Sleet And Thunder',
    'lightsnowandthunder': 'Light Snow And Thunder',
    'heavysnowandthunder': 'Heavy Snow And Thunder',
    'lightrainshowers_day': 'Light Rain Showers Day',
    'lightrainshowers_night': 'Light Rain Showers Night',
    'lightrainshowers_polartwilight': 'Light Rain Showers Polar Twilight',
    'heavyrainshowers_day': 'Heavy Rain Showers Day',
    'heavyrainshowers_night': 'Heavy Rain Showers Night',
    'heavyrainshowers_polartwilight': 'Heavy Rain Showers Polar Twilight',
    'lightsleetshowers_day': 'Light Sleet Showers Day',
    'lightsleetshowers_night': 'Light Sleet Showers Day',
    'lightsleetshowers_polartwilight': 'Light Sleet Showers Polar Twilight',
    'heavysleetshowers_day': 'Heavy Sleet Showers Day',
    'heavysleetshowers_night': 'Heavy Sleet Showers Night',
    'heavysleetshowers_polartwilight': 'Heavy Sleet Showers Polar Twilight',
    'lightsnowshowers_day': 'Light Snow Showers Day',
    'lightsnowshowers_night': 'Light Snow Showers Night',
    'lightsnowshowers_polartwilight': 'Light Snow Showers Polar Twilight',
    'heavysnowshowers_day': 'Heavy Snow Showers Day',
    'heavysnowshowers_night': 'Heavy Snow Showers Night',
    'heavysnowshowers_polartwilight': 'Heavy Snow Showers Polar Twilight',
    'lightrain': 'Light Rain',
    'lightsleet': 'Light Sleet',
    'heavysleet': 'Heavy Sleet',
    'lightsnow': 'Light Snow',
    'heavysnow': 'Heavy Snow'
}

def get_string(key):
    """
    Grab string from string list safely

    Keyword arguments:
    key -- the key value to grab
    """
    try:
        return strings[key]
    except KeyError:
        return 'n/a'

class City:
    """
    Class for the City weather report
    """
    def __init__(self, root, geo):
        self.color = '#ccc'
        self.place_id = geo["place_id"]
        self.frame = Frame(root, bg=self.color, padx=20)
        self.frame.pack(pady=20)
        data = self.fetch_weather(geo)

        # Save units
        self.units = data['properties']['meta']['units']

        # List all measured data periods
        self.periods = []

        # Sort data by period and append it in self.periods
        for period in data['properties']['timeseries']:
            self.periods.append(Period(period))

        weather = f"{get_string(self.periods[0].get_code())} "
        weather += f"{self.periods[0].get_details()['air_temperature']}°"

        name = geo['display_name'].split(', ')
        name = ', '.join(name[0:3] + [name[-1]])

        ttk.Label(self.frame, text=weather).grid(column=0, row=1)
        Label(self.frame, text=name, bg=self.color, font='bold').grid(column=0, row=0)
        Button(self.frame, text='X', fg='red', command=self.remove).grid(column=2, row=0)

    def remove(self):
        """
        Delete and destroy this city
        """
        cities = read('./data/cities.json')
        del cities[str(self.place_id)]
        write('./data/cities.json', cities)
        self.frame.destroy()

    def fetch_weather(self, geo):
        """
        Fetch the weather for the city
        """
        # Fetch data from API using geo coordinates
        link = f"https://api.met.no/weatherapi/locationforecast/2.0/\
compact?lat={geo['lat']}&lon={geo['lon']}"
        data = requests.get(link, timeout=5, headers={
            "User-Agent": "Weather App - https://github.com/Pigges/weatherapp-py"
        })
        # Parse response into JSON
        return data.json()
