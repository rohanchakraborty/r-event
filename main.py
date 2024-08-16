# main.py
from connectors.jsonplaceholder_connector import JSONPlaceholderConnector
from connectors.openweather_connector import OpenWeatherConnector
from transformation.api_transformer import APITransformer
from storage.sql_storage import SQLStorage


def main():
    # Initialize components
    json_connector = JSONPlaceholderConnector()
    weather_connector = OpenWeatherConnector(api_key='YOUR_OPENWEATHER_API_KEY')
    transformer = APITransformer()
    storage = SQLStorage()

    # Create tables if not exist
    storage.create_tables()

    # Fetch and store JSONPlaceholder data
    json_data = json_connector.fetch_data()
    transformed_json = transformer.transform(json_data, source="jsonplaceholder")
    for item in transformed_json:
        storage.insert_post(item['title'], item['body'])

    # Fetch and store OpenWeather data
    weather_data = weather_connector.fetch_data()
    transformed_weather = transformer.transform(weather_data, source="openweather")
    storage.insert_weather(transformed_weather['city'], transformed_weather['temperature'], transformed_weather['weather'])

    # Close storage connection
    storage.close()

    print("Data has been successfully fetched, transformed, and stored.")

if __name__ == "__main__":
    main()
