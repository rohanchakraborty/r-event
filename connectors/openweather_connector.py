# connectors/openweather_connector.py

import requests
from .base_connector import BaseConnector

class OpenWeatherConnector(BaseConnector):
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon

    def fetch_data(self):
        params = {
            'lat': self.lat,
            'lon': self.lon,  # Example of excluding some parts
            'appid': self.api_key
        }
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return response.json()


    def send_data(self, data):
        pass  # Not needed for this connector in the MVP
