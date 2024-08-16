# transformation/api_transformer.py

from transformation.base_transformer import BaseTransformer

class APITransformer(BaseTransformer):
    def transform(self, data, source):
        if source == "jsonplaceholder":
            return [{"title": item["title"], "body": item["body"]} for item in data]
        elif source == "mealdb":
            meal = data["meals"][0]
            return {
                "meal_name": meal["strMeal"],
                "category": meal["strCategory"],
                "area": meal["strArea"],
                "instructions": meal["strInstructions"]
            }
