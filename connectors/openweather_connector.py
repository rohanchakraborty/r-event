# connectors/openweather_connector.py

import requests
from .base_connector import BaseConnector

class OpenWeatherConnector(BaseConnector):
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self):
        params = {
            'q': 'London',
            'appid': self.api_key
        }
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        response.raise_for_status()
        return response.json()

    def send_data(self, data):
        pass  # Not needed for this connector in the MVP
