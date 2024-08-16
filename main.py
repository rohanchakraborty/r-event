# main.py

from connectors.jsonplaceholder_connector import JSONPlaceholderConnector
from connectors.mealdb_connector import MealDBConnector
from transformation.api_transformer import APITransformer
from storage.sql_storage import SQLStorage

def main():
    # Initialize components
    json_connector = JSONPlaceholderConnector()
    mealdb_connector = MealDBConnector()
    transformer = APITransformer()
    storage = SQLStorage()

    # Create tables if not exist
    storage.create_tables()

    # Fetch and store JSONPlaceholder data
    json_data = json_connector.fetch_data()
    transformed_json = transformer.transform(json_data, source="jsonplaceholder")
    for item in transformed_json:
        storage.insert_post(item['title'], item['body'])

    # Fetch and store MealDB data
    meal_data = mealdb_connector.fetch_data()
    transformed_meal = transformer.transform(meal_data, source="mealdb")
    storage.insert_meal(transformed_meal['meal_name'], transformed_meal['category'], transformed_meal['area'], transformed_meal['instructions'])

    # Close storage connection
    storage.close()

    print("Data has been successfully fetched, transformed, and stored.")

if __name__ == "__main__":
    main()
