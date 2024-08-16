# connectors/jsonplaceholder_connector.py

import requests
from .base_connector import BaseConnector

class JSONPlaceholderConnector(BaseConnector):
    def fetch_data(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        return response.json()

    def send_data(self, data):
        pass  # Not needed for this connector in the MVP
