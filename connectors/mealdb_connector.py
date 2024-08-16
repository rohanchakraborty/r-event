# connectors/mealdb_connector.py

import requests
from .base_connector import BaseConnector

class MealDBConnector(BaseConnector):
    def fetch_data(self):
        response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()

    def send_data(self, data):
        pass  # Not needed for this connector in the MVP
